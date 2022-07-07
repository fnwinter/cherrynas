function uploadPopup() {
  $( function() {
    $( "#upload_dialog" ).dialog(
        {
            open: function() {
                $(this).closest(".ui-dialog")
                .find(".ui-dialog-titlebar-close")
                .removeClass("ui-dialog-titlebar-close")
                .addClass("ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close")
                .html("<span class='ui-button-icon ui-icon ui-icon-closethick'></span>");
            },
            width: 400
        }
    );
  });
}
