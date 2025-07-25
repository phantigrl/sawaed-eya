/**
 * Basic client‑side validation + UX touches
 * – Checks file size ≤ 2 MB
 * – Displays instant feedback
 */
document.addEventListener("DOMContentLoaded", () => {
  const form   = document.getElementById("jobForm");
  const msgBox = document.getElementById("formMsg");

  form.addEventListener("submit", e => {
    const cvInput = form.elements["cv"];
    const maxSize = 2 * 1024 * 1024; // 2 MB

    if (cvInput.files.length && cvInput.files[0].size > maxSize) {
      e.preventDefault();
      showMsg("❌ حجم السيرة الذاتية يجب ألا يتجاوز 2 ميغابايت | CV must be ≤ 2 MB", "error");
    } else {
      showMsg("⏳ جاري الإرسال … | Submitting …", "waiting");
    }
  });

  function showMsg(text, type) {
    msgBox.textContent = text;
    msgBox.style.color =
      type === "error"   ? "crimson" :
      type === "waiting" ? "#aa8800" :
      "seagreen";
  }
});
