$(document).ready(function(){
    //usa o plugin datatables para colocar campos de pesquisa, e ordenacao na tabela
    $("#tabela-equipamentos").DataTable({
        // aplica traducao para portugues nos campos da tabela
        responsive: true,
        // "bSort": false,
        "aaSorting": [],
        "pageLength": 50,
        "language": {
            "decimal": "",
            "emptyTable": "Sem dados disponíveis",
            "info": "",
            "infoEmpty": "",
            "infoFiltered": "",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "",
            "loadingRecords": "A carregar dados...",
            "processing": "A processar...",
            "search": "Procurar:",
            "zeroRecords": "Não foram encontrados resultados",
            "paginate": {
                "first": "Primeiro",
                "last": "Último",
                "next": "Seguinte",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": ordem crescente",
                "sortDescending": ": ordem decrescente"
            }
        }
    });

    
    var deleteButtons = document.querySelectorAll('#delete-Button'); // acessa o botao excluir da tabela 
    var modal = document.getElementById('deleteModal'); // carrega o modal de exclusao
    var closeButton = document.querySelector('.close-button'); // botao de fechar o modal
    var confirmDeleteButton = document.getElementById('confirm-delete'); // botao de confirmacao de exclusao do modal 
    var itemDetails = document.getElementById('item-details'); // elemento do modal de exclusão que mostra detalhes da exclusão
    var currentPk; // representa a primary key do item que sera excluido

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // carrega o id e o nome do item a ser excluido
            var itemId = button.getAttribute('itemID');
            var itemName = button.getAttribute('itemName');
            
            // define os detalhes do item no modal antes de motrar na tela
            itemDetails.textContent = `ID: ${itemId}\nNome: ${itemName}`;
            // configura primary key do item a ser excluido
            currentPk = itemId;
            
            // exibe o modal na tela
            modal.style.display = 'block';
        });
    });

    // funcao para fechar o modal pelo botao
    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // fecha o modal quando clica em qualquer lugar da tela 
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });

    // Faz um post com o formulario para deletar o item usando a primary key armazenada em "currentPk"
    confirmDeleteButton.addEventListener('click', function() {
        // envia o post para exclusao
        fetch(`delete/${currentPk}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json()) // aguarda resposta do servidor atraves de um json
        .then(data => {
            // mostra aviso na tela de exclusao concluida do banco e um erro caso nao tenha sido possivel a exclusao
            if (data.success) {
                location.reload();
                alert('Item excluido com sucesso');
            } else {
                alert('Erro ao excluir o item');
            }
        });
        // remove o modal da tela
        modal.style.display = 'none';
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    

});