window.addEventListener("DOMContentLoaded", function () {
  const tryRemoveElements = () => {
    const newChatButton = document.querySelector('#new-chat-button');
    const watermark = document.querySelector('a.watermark'); // هذا هو العنصر الجديد
    const footer = document.querySelector("footer");

    if (newChatButton) {
      newChatButton.style.display = "none";
    }

    if (footer) {
      footer.style.display = "none";
    }

    if (watermark) {
      watermark.style.display = "none"; // أو watermark.remove() للحذف الكامل
    }
  };

  let attempts = 0;
  const interval = setInterval(() => {
    tryRemoveElements();
    attempts++;
    if (attempts > 10) clearInterval(interval);
  }, 500);
});
