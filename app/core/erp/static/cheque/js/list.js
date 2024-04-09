let tblCheque;
function getData(){
    tblCheque = $('#data').DataTable( {
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
            {"data": "numero"},
            {"data": "banco"},
            {"data": "proveedor"},
            {"data": "valor"},
            {"data": "fecha_emision"},
            {"data": "fecha_pago"},
            {"data": "fecha_vto"},
            {"data": "fecha_vto"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row){
                var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit" style="font-size: 10px; padding: 10px"></i></a>   ';
                    buttons += '<a href="#" rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt" style="font-size: 10px; padding: 10px"></i></a>   ';
                    buttons += '<a href="#" rel="cobrar" class="btn btn-success btn-xs btn-flat"><i class="fas fa-dollar-sign" style="font-size: 10px; padding: 10px"></i></a>';
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
        modal_title.find('span').html('Creación de un cheque');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalCheque').modal('show');
    });
    $('#data tbody').on('click' ,'a[rel="edit"]', function(){
        modal_title.find('span').html('Edición de un Cheque');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblCheque.cell( $ (this).closest('td, li')).index();
        var data = tblCheque.row(tr.row).data();
        console.log(data);
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="numero"]').val(data.numero);

        $('select[name="banco"]').val(data.banco);

        $('select[name="proveedor"]').val(data.proveedor);

        $('input[name="valor"]').val(data.valor);
        $('input[name="fecha_emision"]').val(data.fecha_emision);
        $('input[name="fecha_pago"]').val(data.fecha_pago);
        $('input[name="fecha_vto"]').val(data.fecha_vto);


        $('#myModalCheque').modal('show');
    });


    $('#data tbody').on('click' ,'a[rel="delete"]', function(){
        var tr = tblCheque.cell( $ (this).closest('td, li')).index();
        var data = tblCheque.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de eliminar el cheque seleccionado?', parameters, function () {
            tblCheque.ajax.reload();
        });
    });

        $('#myModalCheque').on('shown.bs.modal', function () {
        //$('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalCheque').modal('hide');
            tblCheque.ajax.reload();
        });
    });
});