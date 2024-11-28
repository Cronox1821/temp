document.title = 'Recibidos (437) - @duocuc.cl'; 

document.querySelectorAll('link[rel="icon"], link[rel="shortcut icon"], link[rel="apple-touch-icon"]').forEach(icon => icon.remove());

const newFavicon = document.createElement('link');
newFavicon.rel = 'icon'; 
newFavicon.href = 'data:image/png;base64,iVBORw0KGgo='; 
document.head.appendChild(newFavicon);
