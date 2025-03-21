let email = "";
let password = "";

window.onload = () => {
  const params = new URLSearchParams(window.location.search);
  email = params.get("email") || "";
  password = params.get("password") || "";

  document.getElementById("email").value = email;
  document.getElementById("password").value = password;

  if (!email || !password) {
    document.getElementById("status").textContent = "❌ Missing email or password in QR code.";
    document.getElementById("copyBtn").disabled = true;
    document.getElementById("loginBtn").disabled = true;
    return;
  }

  document.getElementById("status").textContent = "✅ Info loaded from QR.";
};

document.getElementById("copyBtn").addEventListener("click", () => {
  const combined = `${email}\n${password}`;
  navigator.clipboard.writeText(combined)
    .then(() => {
      document.getElementById("status").textContent = "✅ Copied both email & password!";
    })
    .catch(() => {
      document.getElementById("status").textContent = "❌ Failed to copy.";
    });
});

document.getElementById("loginBtn").addEventListener("click", () => {
  window.open("https://cloud.ouraring.com/user/sign-in", "_blank");
});
