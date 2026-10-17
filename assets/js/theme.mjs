/* System / light / dark, using system fonts and zero remote design dependencies. */
const choices = ["system", "light", "dark"];
let selected = "system";
try { const saved = localStorage.getItem("ekguru.theme.v1"); if (choices.includes(saved)) selected = saved; } catch { /* private mode */ }
const button = document.querySelector("[data-theme-toggle]");
function apply() {
  document.documentElement.dataset.theme = selected;
  if (!button) return;
  button.textContent = ({ system: "◐", light: "☀", dark: "☾" })[selected];
  button.setAttribute("aria-label", `Theme: ${selected}. Switch to ${choices[(choices.indexOf(selected) + 1) % choices.length]}`);
  button.title = `Appearance: ${selected}`;
}
button?.addEventListener("click", () => { selected = choices[(choices.indexOf(selected) + 1) % choices.length]; apply(); try { localStorage.setItem("ekguru.theme.v1", selected); } catch { /* still works for this tab */ } });
apply();
