function redirect(request) {
    const prefix = 'http://go/';
    const path = request.url.slice(prefix.length);
    return { redirectUrl: 'http://127.0.0.1:61234/go/' + path };
}

chrome.webRequest.onBeforeRequest.addListener(redirect, { urls: ['http://go/*']}, ['blocking']);