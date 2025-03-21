let email = "";
let password = "";

window.onload = () => {
  const params = new URLSearchParams(window.location.search);
  email = params.get("email") || "";
  password = params.get("password") || "";

  if (!email || !password) {
    document.body.innerHTML = "<h2>❌ Invalid QR code: missing email or password.</h2>";
    return;
  }

  document.getElementById("emailDisplay").textContent = email;
  document.getElementById("passwordDisplay").textContent = password;

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.open("https://cloud.ouraring.com/user/sign-in", "_blank");
  });
};

function copyToClipboard(type) {
  const value = type === 'email' ? email : password;

  navigator.clipboard.writeText(value)
    .then(() => {
      document.getElementById("status").textContent = `✅ ${type.charAt(0).toUpperCase() + type.slice(1)} copied!`;
    })
    .catch(err => {
      document.getElementById("status").textContent = `❌ Failed to copy ${type}.`;
      console.error(err);
    });
}
