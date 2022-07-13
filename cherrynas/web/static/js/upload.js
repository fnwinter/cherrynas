function showUploadPopup() {
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
            width: 400
        }
    );
  });
}

var upload_file_list = [];

$(function() {
    fileDropDown();
    clearList();
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
      var name = input_file.files.item(i).name;
      alert("file name: " + name);
    }
}

function updateDragFiles(fileObject) {

}

function submitFiles() {
    $('#uploadImage').submit(function(event){
        $(this).ajaxSubmit({
            target: '#targetLayer',
            beforeSubmit:function(){
                $('.progress-bar').width('50%');
            },
            uploadProgress: function(event, position, total, percentageComplete)
            {
                $('.progress-bar').animate({
                    width: percentageComplete + '%'
                }, {
                    duration: 1000
                });
            },
            success:function(data){

            },
            resetForm: true
        });
      });
}

function updateList() {
}

function clearList() {
}
