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

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.open("https://cloud.ouraring.com/user/sign-in", "_blank");
  });
};

function copyOne(type) {
  const value = type === "email" ? email : password;

  navigator.clipboard.writeText(value).then(() => {
    document.getElementById("status").textContent = `✅ ${type.charAt(0).toUpperCase() + type.slice(1)} copied to clipboard.`;
  }).catch((err) => {
    document.getElementById("status").textContent = "❌ Could not copy.";
    console.error(err);
  });
}
