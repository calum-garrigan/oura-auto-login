let email = "";
let password = "";

window.onload = () => {
  const urlParams = new URLSearchParams(window.location.search);
  email = urlParams.get("email") || "";
  password = urlParams.get("password") || "";

  document.getElementById("emailDisplay").textContent = email;
  document.getElementById("passwordDisplay").textContent = password;

  if (!email || !password) {
    document.body.innerHTML = "<h2>❌ Missing email or password in the QR code URL.</h2>";
    return;
  }

  copyToClipboard();

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.open("https://cloud.ouraring.com/user/sign-in", "_blank");
  });
};

function copyToClipboard() {
  const combined = `${email}\n${password}`;
  navigator.clipboard.writeText(combined).then(() => {
    document.getElementById("status").textContent = "✅ Copied both email and password to clipboard.";
  }).catch((err) => {
    document.getElementById("status").textContent = "❌ Could not copy to clipboard.";
    console.error(err);
  });
}
