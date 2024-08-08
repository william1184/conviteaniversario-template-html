# Criação de convite personalizado

Foi criado um convite .html personalizado que possui um javascript que faz a confirmação em um excel do google sheet.

# Pontos principais
- O convite possui mapa do google maps
    - https://support.google.com/maps/answer/7101463?hl=pt-BR&co=GENIE.Platform%3DDesktop
- O convite possui botão de whatsapp
- O convite armazena no localstorage a confirmação
    - https://developer.mozilla.org/pt-BR/docs/Web/API/Window/localStorage
- O convite envia um post para visualização
- A imagem de background está em base64 
    - https://base64.guru/converter/encode/image
- Icones estão como inline SVG
    - https://icons.getbootstrap.com/
- Foi adicionado o css de borboletas
    - https://jaron.nl/articles/animate-butterfly
- Foi adicionado o css de uma flor desabrocando
    - https://www.codewithrandom.com/2023/11/17/blossoming-flowers-using-css/

## Integrando com google sheet

Integrar uma webpage com Google Sheets pode ser muito útil para armazenar dados de RSVP diretamente na planilha. Para isso, podemos usar o Google Apps Script. Aqui está um exemplo de como fazer isso:

1. Criar o Google Sheet e o Google Apps Script

    - a. Crie uma nova planilha no Google Sheets.
    - b. Vá para "Extensões" > "Apps Script".
    - c. No editor de scripts, substitua o código padrão pelo seguinte:

        ``` javascript
        function doPost(e) {
            var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
            var params = JSON.parse(e.postData.contents);
            
            var date = new Date();
            var formattedDate = Utilities.formatDate(date, Session.getScriptTimeZone(), 'dd/MM/yyyy HH:mm:ss');
            
            sheet.appendRow([params.nome, params.telefone, params.presenca, formattedDate]);
            
            return ContentService.createTextOutput(JSON.stringify({ 'status': 'sucesso' }))
                .setMimeType(ContentService.MimeType.JSON)
                .setHeaders({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'Content-Type'
                });
        }
        ``` 
    - d. Salve o script e implante-o como um aplicativo web. Vá para "Publicar" > "Implantar como aplicativo web". Selecione "Qualquer um, mesmo anônimo" como quem pode acessar.
2. Obter a URL do seu aplicativo web
    - a. Após a implantação, copie a URL fornecida.

3. Editar o HTML para integrar com o Google Sheets
    Aqui está o código HTML atualizado que envia dados para o Google Sheets:
    ``` javascript
        <script>
            function rsvp() {
                const nome = document.getElementById('nome').value;
                if (!nome) {
                    alert('Por favor, insira seu nome.');
                    return;
                }
                
                fetch('URL_DO_SEU_APP_SCRIPT', { // Substitua pela URL do seu App Script
                    method: 'POST',
                    body: JSON.stringify({ nome: nome, presenca: 'Confirmado' }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'sucesso') {
                        alert('Sua presença foi confirmada! Aguardamos você no Jardim Encantado!');
                    } else {
                        alert('Houve um problema ao confirmar sua presença. Tente novamente.');
                    }
                })
                .catch(error => {
                    alert('Erro: ' + error);
                });
            }
        </script>

    ```

* Lembre-se de substituir URL_DO_SEU_APP_SCRIPT pela URL real do seu Google Apps Script.

