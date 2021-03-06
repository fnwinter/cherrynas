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