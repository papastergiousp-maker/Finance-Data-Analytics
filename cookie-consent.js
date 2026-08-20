/**
 * PhytAI Portfolio & Tools - Universal Cookie & Analytics Consent
 * Supports: Google Analytics (gtag.js) & Microsoft Clarity
 */
(function () {
  const CONSENT_KEY = 'phytai_cookie_consent';

  // Check if consent has already been given
  if (localStorage.getItem(CONSENT_KEY)) {
    return;
  }

  // Detect language
  const isGreek = (document.documentElement.lang === 'el') || (localStorage.getItem('site_lang') === 'greek') || (localStorage.getItem('cv_lang') === 'greek');

  const bannerText = isGreek
    ? '🍪 <strong>Πολιτική Cookies & Analytics:</strong> Χρησιμοποιούμε βασικά cookies και ανώνυμα εργαλεία ανάλυσης (Google Analytics & Microsoft Clarity) για τη βελτίωση της εμπειρίας σας.'
    : '🍪 <strong>Cookie & Analytics Policy:</strong> We use basic cookies and anonymous analytics (Google Analytics & Microsoft Clarity) to optimize user experience.';

  const acceptText = isGreek ? 'Αποδοχή Όλων' : 'Accept All';
  const necessaryText = isGreek ? 'Μόνο Απαραίτητα' : 'Necessary Only';

  function createBanner() {
    const banner = document.createElement('div');
    banner.id = 'phytai-cookie-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '18px';
    banner.style.left = '18px';
    banner.style.right = '18px';
    banner.style.maxWidth = '540px';
    banner.style.margin = '0 auto';
    banner.style.backgroundColor = 'rgba(15, 23, 42, 0.96)';
    banner.style.backdropFilter = 'blur(12px)';
    banner.style.webkitBackdropFilter = 'blur(12px)';
    banner.style.border = '1px solid rgba(255, 255, 255, 0.15)';
    banner.style.borderRadius = '16px';
    banner.style.padding = '16px 20px';
    banner.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255,255,255,0.05)';
    banner.style.zIndex = '999999';
    banner.style.fontFamily = "'Segoe UI', system-ui, -apple-system, sans-serif";
    banner.style.color = '#e2e8f0';
    banner.style.fontSize = '13px';
    banner.style.lineHeight = '1.5';
    banner.style.opacity = '0';
    banner.style.transform = 'translateY(20px)';
    banner.style.transition = 'opacity 0.35s ease, transform 0.35s ease';

    banner.innerHTML = `
      <div style="margin-bottom: 12px; color: #cbd5e1;">
        ${bannerText}
      </div>
      <div style="display: flex; justify-content: flex-end; gap: 8px; flex-wrap: wrap;">
        <button id="phytai-cookie-necessary" style="
          background: transparent;
          color: #94a3b8;
          border: 1px solid rgba(255, 255, 255, 0.18);
          border-radius: 8px;
          padding: 6px 14px;
          font-size: 12px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        ">${necessaryText}</button>
        <button id="phytai-cookie-accept" style="
          background: linear-gradient(135deg, #10b981, #059669);
          color: #ffffff;
          border: none;
          border-radius: 8px;
          padding: 6px 18px;
          font-size: 12px;
          font-weight: 700;
          cursor: pointer;
          box-shadow: 0 2px 8px rgba(16, 185, 129, 0.35);
          transition: all 0.2s;
        ">✓ ${acceptText}</button>
      </div>
    `;

    document.body.appendChild(banner);

    // Animate in
    setTimeout(() => {
      banner.style.opacity = '1';
      banner.style.transform = 'translateY(0)';
    }, 600);

    // Event listeners
    const closeBanner = () => {
      banner.style.opacity = '0';
      banner.style.transform = 'translateY(20px)';
      setTimeout(() => {
        if (banner.parentNode) banner.parentNode.removeChild(banner);
      }, 350);
    };

    document.getElementById('phytai-cookie-accept').addEventListener('click', function () {
      localStorage.setItem(CONSENT_KEY, 'accepted');
      if (window.clarity) clarity('set', 'cookie_consent', 'accepted');
      if (window.gtag) gtag('consent', 'update', { analytics_storage: 'granted' });
      closeBanner();
    });

    document.getElementById('phytai-cookie-necessary').addEventListener('click', function () {
      localStorage.setItem(CONSENT_KEY, 'necessary');
      if (window.clarity) clarity('set', 'cookie_consent', 'necessary');
      closeBanner();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createBanner);
  } else {
    createBanner();
  }
})();
