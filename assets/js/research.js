(() => {
  const toggles = Array.from(document.querySelectorAll(".abstract-toggle"));

  const closeAbstract = (toggle) => {
    const panel = document.getElementById(toggle.getAttribute("aria-controls"));
    if (!panel) return;

    toggle.setAttribute("aria-expanded", "false");
    toggle.textContent = "Abstract";
    panel.hidden = true;
  };

  toggles.forEach((toggle) => {
    toggle.addEventListener("click", () => {
      const panel = document.getElementById(toggle.getAttribute("aria-controls"));
      if (!panel) return;

      const shouldOpen = toggle.getAttribute("aria-expanded") !== "true";
      toggles.forEach(closeAbstract);

      if (shouldOpen) {
        toggle.setAttribute("aria-expanded", "true");
        toggle.textContent = "Close";
        panel.hidden = false;
      }
    });
  });
})();
