window.onload = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const email = urlParams.get("email");
  const password = urlParams.get("password");

  if (email && password) {
    const loginInfo = `${email}\n${password}`;

    navigator.clipboard.writeText(loginInfo).then(() => {
      console.log("✅ Credentials copied to clipboard.");
    }).catch((err) => {
      console.error("❌ Clipboard copy failed:", err);
    });
  } else {
    document.body.innerHTML = "<h2>❌ Missing login credentials in the QR code URL.</h2>";
  }

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.location.href = "https://cloud.ouraring.com/user/sign-in";
  });
};
