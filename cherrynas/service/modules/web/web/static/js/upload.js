function showUploadPopup() {
  upload_file_list = [];
  $( function() {
    $( "#upload_dialog" ).dialog(
        {
            open: function() {
                $(this).closest(".ui-dialog")
                .find(".ui-dialog-titlebar-close")
                .removeClass("ui-dialog-titlebar-close")
                .addClass("ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close")
                .html("<span class='ui-button-icon ui-icon ui-icon-closethick'></span>");

                $("#upload_dialog").removeClass("ui-dialog-content");
            },
            close: function() {
                location.reload();
            },
            width: 400
        }
    );
  });
}

var upload_file_list = [];

$(function() {
    fileDropDown();
});

function fileDropDown() {
    var dropZone = $("#dropZone");
    dropZone.on('dragenter', function(e) {
        e.stopPropagation();
        e.preventDefault();
        dropZone.css('background-color', '#E3F2FC');
    });
    dropZone.on('dragleave', function(e) {
        e.stopPropagation();
        e.preventDefault();
        dropZone.css('background-color', '#FFFFFF');
    });
    dropZone.on('dragover', function(e) {
        e.stopPropagation();
        e.preventDefault();
        dropZone.css('background-color', '#E3F2FC');
    });
    dropZone.on('drop', function(e) {
        e.preventDefault();
        dropZone.css('background-color', '#FFFFFF');
        var files = e.originalEvent.dataTransfer.files;
        if (files != null) {
            if (files.length < 1) {
                return;
            } else {
                updateDragFiles(files)
            }
        }
    });
}

function updateInputFiles() {
    var input_file = document.getElementById('uploadFiles');
    for (var i = 0; i < input_file.files.length; ++i) {
        let file = input_file.files.item(i);
        upload_file_list.push(file);
    }
    updateList();
}

function updateDragFiles(files) {
    for (var i = 0; i < files.length; ++i) {
        upload_file_list.push(files[i]);
    }
    updateList();
}

function submitFiles() {
    for (let i = 0; i < upload_file_list.length; ++i)
    {
        var formData = new FormData(uploadImage);
        let file = upload_file_list[i];
        formData.append("uploadFile_" + i,file);
        formData.append("id", `file_upload_complete_${i}`)
        $.ajax({
            url: '/cherry/explorer/uploadFile',
            data: formData,
            type: 'POST',
            contentType: false,
            processData: false,
            success: function(data, txtStatus, jqXHR) {
                let id = $(this)[0].data.get('id');
                console.log(id);
                $(`#${id}`).text("Done");
            }
        });
    }
}

function updateList() {
    $("#uploadList tbody tr").remove();
    for (let i = 0; i < upload_file_list.length; ++i)
    {
        let file = upload_file_list[i];
        let file_id = i;
        let file_name = file.name;
        let file_size = file.size;
        let row = `"<tr id='file_${file_id}'><th scope='row'>${file_id}</th>`+
            `<td>${file_name}</td><td>${file_size}</td><td id='file_upload_complete_${file_id}'>Wait</td></tr>`;
        $("#uploadList tbody").append(row)
    }
}

function clearList() {
    upload_file_list = [];
    $('#uploadList tbody tr').remove();
}
