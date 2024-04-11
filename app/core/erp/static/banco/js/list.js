let tblBanco
function getData(){
    tblBanco = $('#data').DataTable( {
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
            {"data": "nombre"},
            {"data": "detalle"},
            {"data": "detalle"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row){
                var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat" title="Editar"><i class="fas fa-edit" style="font-size: 12px; padding: 10px"></i></a>   ';
                    buttons += '<a href="#" rel="delete" class="btn btn-danger btn-xs btn-flat" title="Eliminar"><i class="fas fa-trash-alt" style="font-size: 12px; padding: 10px"></i></a>   ';
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
        modal_title.find('span').html('Creación de un Banco Origen');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalBanco').modal('show');
    });

    $('#data tbody').on('click' ,'a[rel="edit"]', function(){
        modal_title.find('span').html('Edición de un Banco');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblBanco.cell( $ (this).closest('td, li')).index();
        var data = tblBanco.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="nombre"]').val(data.nombre);
        $('input[name="detalle"]').val(data.detalle);
        $('#myModalBanco').modal('show');

    });
    $('#data tbody').on('click' ,'a[rel="delete"]', function(){
        var tr = tblBanco.cell( $ (this).closest('td, li')).index();
        var data = tblBanco.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de eliminar el registro seleccionado?', parameters, function () {
            tblBanco.ajax.reload();
        });
    });

        $('#myModalBanco').on('shown.bs.modal', function () {
        //$('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalBanco').modal('hide');
            tblBanco.ajax.reload();
        });
    });
});