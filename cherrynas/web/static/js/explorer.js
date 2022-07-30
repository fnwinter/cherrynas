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
  });
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

function renameItem() {
  $( function() {
    alert("TEST");
    $( "#rename_file_dialog" ).show();
  });
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