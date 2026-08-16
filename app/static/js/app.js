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
