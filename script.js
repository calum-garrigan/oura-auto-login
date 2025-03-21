document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const email = params.get("email");
  const password = params.get("password");

  const emailField = document.getElementById("email");
  const passwordField = document.getElementById("password");
  const status = document.getElementById("status");

  if (!email || !password) {
    status.textContent = "❌ Missing email or password in QR link.";
    document.getElementById("copyBtn").disabled = true;
    document.getElementById("loginBtn").disabled = true;
    return;
  }

  emailField.value = email;
  passwordField.value = password;
  status.textContent = "✅ Info loaded from QR.";

  document.getElementById("copyBtn").addEventListener("click", () => {
    const combined = `${email}\n${password}`;
    navigator.clipboard.writeText(combined).then(() => {
      status.textContent = "✅ Copied both email & password!";
    }).catch(() => {
      status.textContent = "❌ Failed to copy to clipboard.";
    });
  });

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.open("https://cloud.ouraring.com/user/sign-in", "_blank");
  });
});
