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

function show_error_dialog(title, content) {
  $( "#error_msg" ).show();
  $('#error_msg_title').text(title);
  $('#error_msg_content').text(content);
}
function close_error_dialog() {
  $( "#error_msg" ).hide();
}

function newFolder() {
    $( "#new_folder_dialog" ).dialog(
        {
            open: function() {
                $(this).closest(".ui-dialog")
                .find(".ui-dialog-titlebar-close")
                .removeClass("ui-dialog-titlebar-close")
                .addClass("ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close")
                .html("<span class='ui-button-icon ui-icon ui-icon-closethick'></span>");

                $("#new_folder_dialog").removeClass("ui-dialog-content");
            },
            close: function() {
                location.reload();
            },
            width: 400
        }
    );
}

function copyItem() {
    $( "#exampleModal" ).dialog();
}

function pasteItem() {

}

function deleteItem() {
    let items = get_selected_items();
    console.log(items);
    send_command("delete_item", items);
    //location.reload();
}

function showNameDialog(title, placeholder, callback) {
    var return_val = '';

    $( "#name_dialog_label").text(title);
    $( "#file_folder_name").attr('placeholder', placeholder);

    $( "#name_dialog" ).dialog(
        {
            open: function() {
                $(this).closest(".ui-dialog")
                .find(".ui-dialog-titlebar-close")
                .removeClass("ui-dialog-titlebar-close")
                .addClass("ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close")
                .html("<span class='ui-button-icon ui-icon ui-icon-closethick'></span>");
                $("#name_dialog").removeClass("ui-dialog-content");
            },
            close: function() {
                return_val = $("#file_folder_name").val();
                callback(return_val);
                location.reload();
            },
            width: 400
        }
    );
    return return_val;
}

function closeNameDialog() {
    $( "#name_dialog" ).dialog("close");
}

function renameItem() {
    var items = get_selected_items();
    if (items.length != 1) {
        show_error_dialog("Rename", "A file is not selected. or multiple files are selected.");
    } else {
        showNameDialog("Rename", items[0],
        function (new_name) {
            if (new_name.length != 0 && items[0].length != 0) {
                send_command("rename_item", {"origin": items[0], "new": new_name });
            }
        });
    }
}

function send_command(_command, _option) {
  let request_url =  location.href + 'command';
  axios.get(request_url,{
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