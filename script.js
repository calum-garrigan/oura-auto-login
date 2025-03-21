let email = "";
let password = "";

window.onload = () => {
  const params = new URLSearchParams(window.location.search);
  email = params.get("email") || "";
  password = params.get("password") || "";

  if (!email || !password) {
    document.body.innerHTML = "<h2>❌ Invalid QR link: missing email or password.</h2>";
    return;
  }

  document.getElementById("emailDisplay").textContent = email;
  document.getElementById("passwordDisplay").textContent = password;

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.open("https://cloud.ouraring.com/user/sign-in", "_blank");
  });
};

function copyBoth() {
  const combined = `Email: ${email}\nPassword: ${password}`;
  navigator.clipboard.writeText(combined)
    .then(() => {
      document.getElementById("status").textContent = "✅ Copied both email & password!";
    })
    .catch(err => {
      document.getElementById("status").textContent = "❌ Failed to copy.";
      console.error(err);
    });
}
