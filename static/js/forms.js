function readBarCode(id) {
    $('#barCodeReader').css("display","block");
    $('#close-button').on('click', () => {
        $('#barCodeReader').css("display","none")
        Quagga.stop();
    });
    $(window).on('click', (event) => {
        if(event.target == $('#barCodeReader')[0]){
            $('#barCodeReader').css("display","none");
            Quagga.stop();
        }
    });

    Quagga.init({
        inputStream: {
            name: "Live",
            type: "LiveStream",
            target: document.querySelector('#cam'),    // Or '#yourElement' (optional)
            constraints: {
                width: 640,
                height: 480,
            },
        },
        decoder: {
            readers: ["code_128_reader"]
        }
    }, function (err) {
        if (err) {
            console.log(err);
            return
        }
        
        Quagga.start();
    });

    Quagga.onDetected((data) => {
        // fecha o modal
        $('#barCodeReader').css("display","none");
        // para a leitura da camera
        Quagga.stop();

        // abre o campo de inserir equipamentos
        let campo = $(id);
        campo.select2('open');
        // encontra o input no html resposavel pelos id's de equipamentos
        let parent = campo[0].parentElement;
        let input = $(parent).find('input.select2-search__field');

        // adiciona a entrada lida no barcode
        input.val(data.codeResult.code);

        // aciona um evento para atualizar a lista de busca
        input.trigger('input');

    });
}

$(document).ready(function () {

    // Carrega todos os elementos existentes em nossos formularios e aplica a classe css adequada
    try{
        $('#id_id').toggleClass("form-control");
    }catch(e){

    }
    try{
        $('#id_nome').toggleClass("form-control");   
    }catch(e){

    }

    try{
        $('#id_descricao').toggleClass("form-control");
    }catch(e){

    }

    try{
        $('#id_localizacao').toggleClass("form-control");
    }catch(e){

    }

    try{
        $('#id_unidade_de_medida').toggleClass("form-control");
    }catch(e){

    }

    try{
        $('#id_valor').toggleClass("form-control");
    }catch(e){
        
    }
    // parte responsavel pelo formulario de emprestimos
    try{
        $('#id_data_de_devolucao').toggleClass("form-control");

        // usando a biblioteca select2 do jquery possibilida digitar o id do funcionario ou a matricula do aluno ao mesmo tempo que seleciona a opcao
        $('#id_aluno').select2({
            placeholder: 'Selecione um Aluno ou digite sua Matricula',
            allowClear: true,
            width: '100%'
        });

        $('#id_funcionario').select2({
            placeholder: 'Selecione um funcionário ou digite o ID',
            allowClear: true,
            width: '100%'
        });

        $('#id_equipamentos').select2({
            placeholder: 'Selecione os equipamentos ou digite o ID',
            allowClear: true,
            width: '100%',
            multiple: true
        });

        $('#id_componentes').select2({
            placeholder: 'Selecione os componentes ou pesquise por seus parametros',
            allowClear: true,
            width: '100%',
            multiple: true
        });

        $('#id_componentes').on('change', function() {
            var selectedComponents = $(this).val();
            $('#quantidades').empty();  // Limpa os campos de quantidade existentes
        
            if (selectedComponents) {
                selectedComponents.forEach(function(componenteId) {
                    var label = $(`#id_componentes option[value="${componenteId}"]`).text();
                    $('#quantidades').append(`
                        <div class="col">
                            <span>${label}</span>
                            <input class="form-control" type="number" name="quantidade_${componenteId}" id="quantidade_${componenteId}" min="1" placeholder="Quantidade">
                        </div>
                    `);
                });
            }
        });
        

        $('#equipamentoReader').on('click', () => readBarCode('#id_equipamentos'));
        $('#alunoReader').on('click', () => readBarCode('#id_aluno'));

    }catch(e){

    }

});