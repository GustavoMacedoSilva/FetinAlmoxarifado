$(document).ready(function () {

    // Carrega todos os elementos existentes em nossos formularios e aplica a classe css adequada
    try{
        let id_label = document.getElementById("id_id");
        id_label.classList.add("form-control");
    }catch(e){

    }
    try{   
        let name_label = document.getElementById("id_nome");
        name_label.classList.add("form-control");
    }catch(e){

    }

    try{
        let desc_label = document.getElementById("id_descricao");
        desc_label.classList.add("form-control");
    }catch(e){

    }

    try{
        let local_label = document.getElementById("id_localizacao");
        local_label.classList.add("form-control");
    }catch(e){

    }

    try{
        let unidade_label = document.getElementById("id_unidade_de_medida");
        unidade_label.classList.add("form-control");
    }catch(e){

    }

    try{
        let value_label = document.getElementById("id_valor");
        value_label.classList.add("form-control");
    }catch(e){
        
    }

});