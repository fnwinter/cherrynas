$( function() {
  $( "#draggable" ).draggable();
});

var selected_items = [];
$( function() {
  $( "#selectable" ).selectable({
    start: function( event, ui ) {
      selected_items = [];
    },
    selected: function(event, ui) {
      selected_items.push($(ui.selected).text());
    }       
  });
});

function get_selected_items()
{
  let tmp = []
  for (let i in selected_items)
  {
    let item = selected_items[i];
    if (item.trim() == '') continue;
    tmp.push(item.trim());
  }
  let removeDuplicates = new Set(tmp);
  selected_items = [ ...removeDuplicates ];
  return selected_items
}

$('#selectable').selectable({ 
  cancel: '.ui-selected'
});

$('.ui-selected').on('click', function() {
  $(this)
    .removeClass('ui-selected')
    .parents('.ui-selectable')
    .trigger('selectablestop');
});

$( function() {
  $( "li.double_click" ).dblclick(function(object) {
    let double_clicked_item = object.target.textContent.trim()
    send_command("double_click", double_clicked_item);
  });
} );

function newFolder() {
  $( function() {
    $( "#name_dialog" ).dialog(
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
                send_command("create_new_folder", "new_folder_name");
                location.reload();
            },
            width: 400
        }
    );
  });
}

function copyItem() {
    alert("copyFile");
}

function pasteItem() {
    alert("pasteFile");
}

function deleteItem() {
    alert("deleteFile");
}

function renameItem() {
    alert("renameFile");
}

function send_command(_command, _option) {
  axios.get('/explorer/command',{
      params: {
        command: _command,
        option: _option
    }
  })
  .then(response => {
    const data = response.data;
    console.log(`result : `, data.result);
    if (data.result == 'refresh') {
      location.reload();
    }
  })
  .catch(error => console.error(error));
}