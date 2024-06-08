const http = require('http');

        const server = http.createServer((req, res) => {
        console.log("Request received: " + JSON.stringify({
            url: req.url,
            method: req.method,
            headers: req.headers,
        }));

        if (req.method === 'HEAD') {
            res.writeHead(200, { 'Content-Type': 'text/x-component' });
            res.end();
        } else if (req.method === 'GET') {
            res.writeHead(302, { 'Location': `http://127.0.0.1:3000/home?token=dea02ab76f73d31e9152de95aabf786f&directory=/`});
            res.end();
        } else {
            res.writeHead(405, { 'Content-Type': 'text/plain' });
            res.end('Method Not Allowed');
        }
        });

        const PORT = 80;
        server.listen(PORT, () => {
        console.log(`Server is listening on port ${PORT}`);
        });