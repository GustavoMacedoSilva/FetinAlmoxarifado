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
    
    }catch(e){

    }

});