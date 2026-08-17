// ── Progress Tracker Global JS ──────────────────────────────

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  // Current date in header
  const dateEl = document.getElementById('current-date');
  if (dateEl) {
    const now = new Date();
    dateEl.textContent = now.toLocaleDateString('en-US', {
      weekday: 'short', month: 'short', day: 'numeric', year: 'numeric'
    });
  }

  // Animate progress bars on load
  document.querySelectorAll('.progress-fill').forEach(bar => {
    const w = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => { bar.style.width = w; }, 100);
  });

  // Animate ring fills
  document.querySelectorAll('.ring-fill').forEach(ring => {
    const offset = ring.getAttribute('stroke-dashoffset');
    const total = ring.getAttribute('stroke-dasharray');
    ring.style.strokeDashoffset = total;
    setTimeout(() => { ring.style.strokeDashoffset = offset; }, 200);
  });

  // Lucide Icons init
  if (window.lucide) {
    lucide.createIcons();
  }
});

// ── Modal helpers ────────────────────────────────────────────
function openModal(id) {
  const overlay = document.getElementById(id);
  if (overlay) {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    if (window.lucide) {
      setTimeout(() => lucide.createIcons(), 20);
    }
  }
}

function closeModal(id) {
  const overlay = document.getElementById(id);
  if (overlay) {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }
}

// Close modal on overlay click
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-overlay')) {
    e.target.classList.remove('open');
    document.body.style.overflow = '';
  }
});

// Close on Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    document.querySelectorAll('.modal-overlay.open').forEach(m => {
      m.classList.remove('open');
      document.body.style.overflow = '';
    });
  }
});

// ── Toast helper ─────────────────────────────────────────────
function showToast(msg, duration = 3000) {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = msg;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.2s ease';
    setTimeout(() => toast.remove(), 220);
  }, duration);
}

// ── Confirm Delete helper ─────────────────────────────────────
function confirmDelete(msg = 'Are you sure you want to delete this?') {
  return window.confirm(msg);
}

// ── Universal Search Autocomplete ──────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('universalSearchInput');
  const dropdown = document.getElementById('searchResultsDropdown');
  let selectedIndex = -1;
  let debounceTimer = null;

  if (!searchInput || !dropdown) return;

  // Keyboard shortcut '/' or 'cmd+k' or 'ctrl+k' to focus search
  document.addEventListener('keydown', (e) => {
    const active = document.activeElement;
    const isInput = active.tagName === 'INPUT' || active.tagName === 'TEXTAREA' || active.isInputPending || active.isContentEditable;
    
    if (e.key === '/' && !isInput) {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    }
    
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    }
  });

  searchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    const query = searchInput.value.trim();

    if (!query) {
      dropdown.innerHTML = '';
      dropdown.classList.remove('open');
      selectedIndex = -1;
      return;
    }

    debounceTimer = setTimeout(() => {
      fetch(`/api/search?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
          renderSearchResults(data.results);
        })
        .catch(err => console.error("Search error:", err));
    }, 180);
  });

  // Handle keyboard navigation inside search results
  searchInput.addEventListener('keydown', (e) => {
    const items = dropdown.querySelectorAll('.search-result-item');
    if (!items.length) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectedIndex = (selectedIndex + 1) % items.length;
      updateSelection(items);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectedIndex = (selectedIndex - 1 + items.length) % items.length;
      updateSelection(items);
    } else if (e.key === 'Enter') {
      if (selectedIndex >= 0 && selectedIndex < items.length) {
        e.preventDefault();
        items[selectedIndex].click();
      }
    } else if (e.key === 'Escape') {
      dropdown.classList.remove('open');
      searchInput.blur();
    }
  });

  // Hide dropdown on click outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('#headerSearch')) {
      dropdown.classList.remove('open');
    }
  });

  // Re-open dropdown on focus if not empty
  searchInput.addEventListener('focus', () => {
    if (searchInput.value.trim() && dropdown.children.length > 0) {
      dropdown.classList.add('open');
    }
  });

  function updateSelection(items) {
    items.forEach((item, idx) => {
      if (idx === selectedIndex) {
        item.classList.add('selected');
        item.scrollIntoView({ block: 'nearest' });
      } else {
        item.classList.remove('selected');
      }
    });
  }

  function renderSearchResults(results) {
    dropdown.innerHTML = '';
    selectedIndex = -1;

    if (!results || !results.length) {
      dropdown.innerHTML = '<div class="search-no-results">No results found</div>';
      dropdown.classList.add('open');
      return;
    }

    // Group results by category
    const groups = {};
    results.forEach(res => {
      if (!groups[res.category]) {
        groups[res.category] = [];
      }
      groups[res.category].push(res);
    });

    // Append to dropdown
    for (const [category, groupItems] of Object.entries(groups)) {
      const header = document.createElement('div');
      header.className = 'search-group-header';
      header.textContent = category;
      dropdown.appendChild(header);

      groupItems.forEach(item => {
        const a = document.createElement('a');
        a.className = 'search-result-item';
        a.href = item.url;
        
        // Clean display category tag
        const displayTag = category.includes('(') ? category.match(/\(([^)]+)\)/)[1] : category;
        const iconName = item.lucide_icon || 'file-text';

        a.innerHTML = `
          <div class="item-icon">
            <i data-lucide="${iconName}" class="icon-sm"></i>
          </div>
          <div class="item-details">
            <div class="item-title">${escapeHTML(item.title)}</div>
            <div class="item-snippet">${escapeHTML(item.snippet || '')}</div>
          </div>
          <span class="badge ${item.badge_class || 'badge-gray'} item-badge">${escapeHTML(displayTag)}</span>
        `;
        dropdown.appendChild(a);
      });
    }

    dropdown.classList.add('open');
    if (window.lucide) {
      lucide.createIcons();
    }
  }

  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
});

// ── Gamification Filter & Celebration Helpers ──────────────────
window.currentCategoryFilter = 'all';
window.currentStatusFilter = 'all';

window.setCategoryFilter = function(category, btn) {
  window.currentCategoryFilter = category;
  // Support both old and new class names
  document.querySelectorAll('.category-tab, .gm-cat-tab').forEach(t => t.classList.remove('active'));
  if (btn) btn.classList.add('active');
  window.filterAchievements();
};

window.setStatusFilter = function(status, btn) {
  window.currentStatusFilter = status;
  // Support both old and new class names
  document.querySelectorAll('.status-chip, .gm-status-chip').forEach(c => c.classList.remove('active'));
  if (btn) btn.classList.add('active');
  window.filterAchievements();
};

window.filterAchievements = function() {
  const searchInput = document.getElementById('questSearchInput');
  const query = searchInput ? searchInput.value.trim().toLowerCase() : '';
  // Support both old .quest-card and new .gm-ach-card class names
  const cards = document.querySelectorAll('#questsContainer .quest-card, #questsContainer .gm-ach-card');
  let visibleCount = 0;

  cards.forEach(card => {
    const cardCategory = card.getAttribute('data-category');
    const isUnlocked = card.getAttribute('data-unlocked') === 'true';
    const cardTitle = card.getAttribute('data-title') || '';
    const cardDesc = card.getAttribute('data-desc') || '';

    // Check category match
    const categoryMatch = (window.currentCategoryFilter === 'all' || cardCategory === window.currentCategoryFilter);

    // Check status match
    let statusMatch = true;
    if (window.currentStatusFilter === 'unlocked') {
      statusMatch = isUnlocked;
    } else if (window.currentStatusFilter === 'in-progress') {
      statusMatch = !isUnlocked;
    }

    // Check search query match
    const searchMatch = !query || cardTitle.includes(query) || cardDesc.includes(query);

    if (categoryMatch && statusMatch && searchMatch) {
      card.style.display = '';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });

  const countEl = document.getElementById('visibleQuestsCount');
  if (countEl) {
    countEl.textContent = visibleCount;
  }
};

// ── Lightweight Confetti Celebration Engine ───────────────────
window.triggerConfetti = function(duration = 2000) {
  const canvas = document.getElementById('gamification-confetti');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const particles = [];
  const colors = ['#2563EB', '#10B981', '#F59E0B', '#EC4899', '#8B5CF6', '#38BDF8', '#FACC15'];
  const particleCount = 75;

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: window.innerWidth / 2 + (Math.random() - 0.5) * 200,
      y: window.innerHeight / 2 + (Math.random() - 0.5) * 100,
      vx: (Math.random() - 0.5) * 14,
      vy: (Math.random() - 0.5) * 14 - 6,
      size: Math.random() * 8 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * 360,
      rotationSpeed: (Math.random() - 0.5) * 12,
      opacity: 1,
      shape: Math.random() > 0.4 ? 'rect' : 'circle',
    });
  }

  const startTime = Date.now();

  function render() {
    const elapsed = Date.now() - startTime;
    if (elapsed > duration) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      return;
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.35; // gravity
      p.vx *= 0.98; // drag
      p.rotation += p.rotationSpeed;
      p.opacity = Math.max(0, 1 - (elapsed / duration));

      ctx.save();
      ctx.globalAlpha = p.opacity;
      ctx.translate(p.x, p.y);
      ctx.rotate((p.rotation * Math.PI) / 180);
      ctx.fillStyle = p.color;

      if (p.shape === 'rect') {
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
      } else {
        ctx.beginPath();
        ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.restore();
    });

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
};


