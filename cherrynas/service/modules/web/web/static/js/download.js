function downloadItem(path) {
    var link = document.createElement("a");
    link.download = name;
    link.href = path;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    delete link;
}

function downloadURI(uri) {
    var selected_items = get_selected_items();
    selected_items.forEach(
        function(item){
            let url_link = uri + '?file=' + item;
            downloadItem(url_link)
        }
    );
 }