$(document).ready(function(){
    //####### Aplicando o DataTables #######
    //usa o plugin datatables para colocar campos de pesquisa, e ordenacao na tabela
    $("#tabela-equipamentos").DataTable({
        // aplica traducao para portugues nos campos da tabela
        responsive: true,
        // "bSort": false,
        "bPaginate": false,
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

    //####### Declarando funcoes #######

    // funcao para acessar o token de validacao de formularios do django
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

    // Função para filtrar itens que estejam com emprestimos
    function filterItems() {
        if ($('input[name="filter"]').is(':checked')) {
            $('tbody tr[emprestimo!="false"]').show();
        } else {
            $('tbody tr[emprestimo!="false"]').hide();
        }
    }

    //####### Declarando variaveis #######

    var deleteButtons = document.querySelectorAll('#delete-Button'); // acessa o botao excluir da tabela 
    var detailButtons = document.querySelectorAll('#detail-button'); // acessa o botao ver detalhes da tabela
    var emprestimoButtons = document.querySelectorAll('#emprestimoButton'); // acessa o botao emprestar da tabela
    var readerButton = document.getElementById('readerButton');
    var deleteModal = document.getElementById('deleteModal'); // carrega o modal de exclusao
    var detailModal = document.getElementById('detailModal'); // carrega o modal de detalhes
    var readerModal = document.getElementById('barCodeReader'); // carrega o modal de leitura de codigo de barras
    var emprestimoModal = document.getElementById('emprestimoModal'); // carrega o modal de emprestimos
    var closeButtonDelete = document.getElementById('close-button-delete'); // botao de fechar o modal
    var closeButtonDetail = document.getElementById('close-button-detail'); // botao de fechar o modal
    var closeButtonEmprestimo = document.getElementById('close-button-emprestimo'); // botao de fechar o modal
    var closeButtonReader = document.getElementById('close-button-reader'); // botao de fechar o modal
    var confirmDeleteButton = document.getElementById('confirm-delete'); // botao de confirmacao de exclusao do modal 
    var currentPk; // representa a primary key do item que sera excluido

    // Evento de mudança para o checkbox
    $('input[name="filter"]').change(filterItems);

    // Aplicar filtro inicialmente depois de carregar a pagina
    filterItems();

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // elemento do modal de exclusão que mostra detalhes da exclusão
            let itemDetails = document.getElementById('item-details'); 
            // carrega o id e o nome do item a ser excluido
            let itemElement = button.parentElement.parentElement;
            let itemId = itemElement.getAttribute('itemID');
            let itemName = itemElement.getAttribute('itemName');
            
            // define os detalhes do item no modal antes de motrar na tela
            itemDetails.textContent = `ID: ${itemId}\nNome: ${itemName}`;
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
            let itemDescription = itemElement.getAttribute('description');
            let itemLocation = itemElement.getAttribute('itemLocation');
            let emprestimoID = itemElement.getAttribute('emprestimo');
            if(emprestimoID == "false"){
                emprestimoID = "Não esta associado a nenhum emprestimo";
            }
            // carrega os campos para mostragem dos atributos
            let atributo1 = document.getElementById('itemId');
            let atributo2 = document.getElementById('itemName');
            let atributo3 = document.getElementById('itemLocation');
            let atributo4 = document.getElementById('itemDescription');
            let atributo5 = document.getElementById('emprestimoID');

            // define os detalhes do item no modal antes de motrar na tela
            atributo1.textContent = `${itemId}`;
            atributo2.textContent = `${itemName}`;
            atributo3.textContent = `${itemLocation}`;
            atributo4.textContent = `${itemDescription}`;
            atributo5.textContent = `${emprestimoID}`;

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
                    // envia o post para adicionar
                    fetch(`addToEmprestimo/${itemId}/${emprestimoID}/`, {
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
                            alert('Equipamento adicionado ao emprestimo com sucesso');
                        } else if(data.error == 405) {
                            alert('Este equipamento ja se encontra em um emprestimo');
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

    // configura o botao de leitura de barCodes
    readerButton.addEventListener('click', function(){
        readerModal.style.display = 'block';
        
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

    // funcao para fechar o modal pelo botao
    closeButtonReader.addEventListener('click', function() {
        readerModal.style.display = 'none';
        Quagga.stop();
    });

    // fecha o modal quando clica em qualquer lugar da tela 
    window.addEventListener('click', function(event) {
        if (event.target == deleteModal || event.target == detailModal || event.target == emprestimoModal || event.target == readerModal) {
            deleteModal.style.display = 'none';
            detailModal.style.display = 'none';
            emprestimoModal.style.display = 'none';
            readerModal.style.display = 'none';
            Quagga.stop();
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
                alert('Não é possivel excluir um equipamento que esteja atualmente em um emprestimo');
            } else {
                alert('Erro ao excluir o item');
            }
        });
        // remove o modal da tela
        deleteModal.style.display = 'none';
    });
    // identifica quando feita uma leitura de codigo de barras atraves da camera
    Quagga.onDetected((data) => {
            
        // encontra o input no html resposavel pela selecao na lista
        let input = $('#dt-search-0'); 

        // fecha o modal
        readerModal.style.display = 'none';

        // para a leitura da camera
        Quagga.stop();

        // adiciona a entrada lida no barcode
        input.val(data.codeResult.code);

        // aciona um evento para atualizar a lista de busca
        input.trigger('input');

    });

});