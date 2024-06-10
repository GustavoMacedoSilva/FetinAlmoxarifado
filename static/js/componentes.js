$(document).ready(function(){
    //usa o plugin datatables para colocar campos de pesquisa, e ordenacao na tabela
    $("#tabela-componentes").DataTable({
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
    var detailButtons = document.querySelectorAll('#detail-button'); // acessa o botao de detalhes da pagina
    var emprestimoButtons = document.querySelectorAll('#emprestimoButton'); // acessa o botao emprestar da tabela
    var deleteModal = document.getElementById('deleteModal'); // carrega o modal de exclusao
    var detailModal = document.getElementById('detailModal'); // carrega o modal de detalhes
    var emprestimoModal = document.getElementById('emprestimoModal'); // carrega o modal de emprestimos
    var closeButtonDelete = document.getElementById('close-button-delete'); // botao de fechar o modal
    var closeButtonDetail = document.getElementById('close-button-detail'); // botao de fechar o modal
    var closeButtonEmprestimo = document.getElementById('close-button-emprestimo'); // botao de fechar o modal
    var confirmDeleteButton = document.getElementById('confirm-delete'); // botao de confirmacao de exclusao do modal 
    var itemDetails = document.getElementById('item-details'); // elemento do modal de exclusão que mostra detalhes da exclusão
    var currentPk; // representa a primary key do item que sera excluido

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // carrega o id e o nome do item a ser excluido
            let itemElement = button.parentElement.parentElement;
            let itemId = itemElement.getAttribute('itemID');
            let itemName = itemElement.getAttribute('itemName');
            let itemValue = itemElement.getAttribute('itemValue');
            let itemUnit = itemElement.getAttribute('itemUnit');
            
            // define os detalhes do item no modal antes de motrar na tela
            itemDetails.textContent = `ID: ${itemId}\n Nome: ${itemName} ${itemValue}${itemUnit}`;
            // configura primary key do item a ser excluido
            currentPk = itemId;
            
            // exibe o modal na tela
            deleteModal.style.display = 'block';
        });
    });

    detailButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // carrega as informacoes do item
            let itemElement = button.parentElement.parentElement;
            let itemId = itemElement.getAttribute('itemID');
            let itemName = itemElement.getAttribute('itemName');
            let itemValue = itemElement.getAttribute('itemValue');
            let itemUnit = itemElement.getAttribute('itemUnit');
            let itemLocation = itemElement.getAttribute('itemLocation');
            // carrega os campos para mostragem dos atributos
            let atributo1 = document.getElementById('itemID');
            let atributo2 = document.getElementById('itemName');
            let atributo3 = document.getElementById('itemValue');
            let atributo4 = document.getElementById('itemLocation');

            // define os detalhes do item no modal antes de motrar na tela
            atributo1.textContent = `${itemId}`;
            atributo2.textContent = `${itemName}`;
            atributo3.textContent = `${itemValue} ${itemUnit}`;
            atributo4.textContent = `${itemLocation}`;
            
            // exibe o modal na tela
            detailModal.style.display = 'block';
        });
    });

    emprestimoButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // carrega id do equipamento
            let itemElement = button.parentElement.parentElement;
            let itemId = itemElement.getAttribute('itemID');
            // carrega o botao de adicionar a emprestimo
            let addEmprestimoButton = document.getElementById('addEmprestimo');
            // carrega o modal de adicionar a emprestimo
            let addEmprestimoModal = document.getElementById('empretimoIDmodal');
            addEmprestimoButton.addEventListener('click', function() {
                // carrega o botao de cancelar 
                let cancelButton = document.getElementById('cancel-add-emprestimo');
                // carrega o botao de confimar adicao
                let confirmButton = document.getElementById('confirm-add-emprestimo');
                confirmButton.addEventListener('click', function() {
                    // le o valor do input numerico referente ao id do emprestimo
                    let emprestimoID = document.getElementById('addEmprestimoID').value;
                    let quantidade = document.getElementById('addEmprestimoQtd').value;
                    // envia o post para adicionar
                    fetch(`addToEmprestimo/${itemId}/${emprestimoID}/${quantidade}/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Content-Type': 'application/json'
                        },
                    })
                    .then(response => response.json()) // aguarda resposta do servidor atraves de um json
                    .then(data => {
                        // mostra aviso na tela de adicao concluida do banco e um erro caso nao tenha sido possivel a adicao
                        if (data.success) {
                            location.reload();
                            alert('Componente adicionado ao emprestimo com sucesso');
                        } else {
                            alert('Não foi possivel encontrar o emprestimo inserido');
                        }
                    });
                    emprestimoModal.style.display = 'none';
                    addEmprestimoModal.style.display = 'none';
                });
                cancelButton.addEventListener('click', button => addEmprestimoModal.style.display = 'none');
                addEmprestimoModal.style.display = 'block';
            });

            emprestimoModal.style.display = 'block';
        });
    });

    // funcao para fechar o modal pelo botao
    closeButtonDelete.addEventListener('click', function() {
        deleteModal.style.display = 'none';
    });
    // funcao para fechar o modal pelo botao
    closeButtonDetail.addEventListener('click', function() {
        detailModal.style.display = 'none';
    });

    // funcao para fechar o modal pelo botao
    closeButtonEmprestimo.addEventListener('click', function() {
        emprestimoModal.style.display = 'none';
    });

    // fecha o modal quando clica em qualquer lugar da tela 
    window.addEventListener('click', function(event) {
        if (event.target == deleteModal || event.target == detailModal || event.target == emprestimoModal) {
            deleteModal.style.display = 'none';
            detailModal.style.display = 'none';
            emprestimoModal.style.display = 'none';
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
            } else if(data.error == 405) {
                alert('Não é possivel excluir um componente que esteja atualemnte em um emprestimo');
            } else {
                alert('Erro ao excluir o item');
            }
        });
        // remove o modal da tela
        deleteModal.style.display = 'none';
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