function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
$(document).ready(function () {
    let port;
    $('#reader').on('click', async () => {
    
        try {
            
            if (!port) {
                port = await navigator.serial.requestPort();  // O usuário seleciona a porta uma vez
                await port.open({ baudRate: 9600 });
                console.log('Abrindo Porta!');
                // Adiciona um delay de 500ms (meio segundo) antes de enviar o comando
                await delay(2000);  
            }
            
            $('#rfidReader').css("display","block");
            $('#close-button-rfid').on('click', () => {
                $('#rfidReader').css("display","none")
            });
            $(window).on('click', (event) => {
                if(event.target == $('#rfidReader')[0]){
                    $('#rfidReader').css("display","none");
                }
            });
    
            const encoder = new TextEncoder();
            const writer = port.writable.getWriter();
            let matricula = $('#reader').attr('matricula');
            await writer.write(encoder.encode("WRITE "+matricula+"\n"));
            writer.releaseLock();
            
    
            const decoder = new TextDecoder();
            const reader = port.readable.getReader();
            
            // le e constroi a string enviada pelo arduino
            while (true) {
                const { value, done} = await reader.read();
                if (done) {
                    console.log('conexão cortada')
                    reader.releaseLock();
                    break;
                }
                let temp = decoder.decode(value);
                temp.trim();
                if (temp == '-1') {
                    alert('Erro na leitura da carteira, por favor tente novamente!');
                    return;
                }
                if (temp == '1') {
                    alert('Carteira associada ao aluno com sucesso!');
                    reader.releaseLock();
                    break;
                }
            
            }
    
            // fecha o modal
            $('#rfidReader').css("display","none");

            window.location.href = 'http://localhost:8000/';
            
    
        } catch (e) {
            console.error('Erro ao conectar ao leitor: ',e);
        } 
    });
});