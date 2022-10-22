function getWebdriver() {
  if (window.navigator) {
    return window.navigator.webdriver;
  } else if (window.window.navigator) {
    return window.window.navigator.webdriver;
  } else {
    return "Not support";
  }
}

console.log(getWebdriver());
