let tblProveedor
function getData(){
    tblProveedor = $('#data').DataTable( {
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "razonsocial"},
            {"data": "cuit"},
            {"data": "cuit"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row){
                var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit" style="font-size: 10px; padding: 10px"></i></a>   ';
                    buttons += '<a href="#" rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt" style="font-size: 10px; padding: 10px"></i></a>   ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
}

$(function () {

    modal_title = $('.modal-title');

    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un Proveedor');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalProveedor').modal('show');
    });

    $('#data tbody').on('click' ,'a[rel="edit"]', function(){
        modal_title.find('span').html('Edición de un Proveedor');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblProveedor.cell( $ (this).closest('td, li')).index();
        var data = tblProveedor.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="razonsocial"]').val(data.razonsocial);
        $('input[name="cuit"]').val(data.cuit);
        $('#myModalProveedor').modal('show');

    });
    $('#data tbody').on('click' ,'a[rel="delete"]', function(){
        var tr = tblProveedor.cell( $ (this).closest('td, li')).index();
        var data = tblProveedor.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de eliminar el registro seleccionado?', parameters, function () {
            tblProveedor.ajax.reload();
        });
    });

        $('#myModalProveedor').on('shown.bs.modal', function () {
        //$('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalProveedor').modal('hide');
            tblProveedor.ajax.reload();
        });
    });
});