window.onload = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const email = urlParams.get("email");
  const password = urlParams.get("password");

  const emailDisplay = document.getElementById("emailDisplay");
  const passwordDisplay = document.getElementById("passwordDisplay");
  const statusText = document.getElementById("status");

  if (email && password) {
    emailDisplay.textContent = email;
    passwordDisplay.textContent = password;

    const loginText = `${email}\n${password}`;
    navigator.clipboard.writeText(loginText).then(() => {
      statusText.textContent = "✅ Credentials copied to clipboard.";
    }).catch((err) => {
      statusText.textContent = "❌ Couldn't copy to clipboard. Please copy manually.";
      console.error(err);
    });
  } else {
    document.body.innerHTML = "<h2>❌ Missing email or password in the QR code link.</h2>";
  }

  document.getElementById("loginBtn").addEventListener("click", () => {
    window.location.href = "https://cloud.ouraring.com/user/sign-in";
  });
};
