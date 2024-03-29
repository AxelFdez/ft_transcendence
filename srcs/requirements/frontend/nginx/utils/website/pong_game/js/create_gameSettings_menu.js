
function create_OnePlayer_input() {

    // Input part --------------------------------------------------------------
    const mainDiv = document.createElement('div');
    mainDiv.id = 'inputDiv';

    let hr = document.createElement('hr');
    hr.classList = 'text-info mt-4';
    mainDiv.appendChild(hr);

    let div = document.createElement('div');
    div.className = 'col d-flex justify-content-center mt-5';
    
    // Creation de l'input
    let input = document.createElement('input');
    input.className = 'form-control border-info w-50';
    input.type = 'text';
    input.id = 'name';
    input.placeholder="Name"

    div.appendChild(input);
    mainDiv.appendChild(div);

    // Creation du bouton
    let playBtn = document.createElement('button');
    playBtn.type = 'button';
    playBtn.className = 'btn btn-outline-success w-25 mb-3 mt-3 p-2';
    playBtn.id = 'playBtn';
    playBtn.textContent = 'Play';

    div = document.createElement('div');
    div.className = 'col d-flex justify-content-center mt-2';
    div.id = 'divBtn';

    div.appendChild(playBtn);
    mainDiv.appendChild(div);

    // Récupération de la section par son ID
    let mySection = document.getElementById('containerGameMenu');
    // Ajout de l'élément div principal à la section spécifiée
    mySection.appendChild(mainDiv);
    initPlayBtn();
}

function create_TwoPlayers_input() {

    // Input part --------------------------------------------------------------
    const mainDiv = document.createElement('div');
    mainDiv.id = 'inputDiv';

    let hr = document.createElement('hr');
    hr.classList = 'text-info mt-4';
    mainDiv.appendChild(hr);

    let div = document.createElement('div');
    div.className = 'col d-flex justify-content-center mt-5';
    
    // Creation de l'input 1
    let input1 = document.createElement('input');
    input1.className = 'form-control border-info w-50 me-2';
    input1.type = 'text';
    input1.id = 'playerName_1';
    input1.placeholder="Player 1"
    div.appendChild(input1);
    mainDiv.appendChild(div);

    // Creation de l'input 2
    let input2 = document.createElement('input');
    input2.className = 'form-control border-info w-50';
    input2.type = 'text';
    input2.id = 'playerName_2';
    input2.placeholder="Player 2"
    div.appendChild(input2);
    mainDiv.appendChild(div);


    // Creation du bouton
    div = document.createElement('div');
    div.className = 'col d-flex justify-content-center mt-2';
    div.id = 'divBtn';
    let playBtn = document.createElement('button');
    playBtn.type = 'button';
    playBtn.className = 'btn btn-outline-success w-25 mb-3 mt-3 p-2';
    playBtn.id = 'playBtn';
    playBtn.textContent = 'Play';

    div.appendChild(playBtn);
    mainDiv.appendChild(div);

    // Récupération de la section par son ID
    let mySection = document.getElementById('containerGameMenu');
    // Ajout de l'élément div principal à la section spécifiée
    mySection.appendChild(mainDiv);
    initPlayBtn();
}


function create_Tournament_mode() {
    
    const div = document.createElement('div');
    div.classList = 'col d-flex justify-content-center m-2';
    div.id = 'tournamentModeBtn';

    // Création des boutons
    let fourPlayersBtn = document.createElement('button');
    fourPlayersBtn.type = 'button';
    fourPlayersBtn.className = 'btn btn-outline-info mx-1';
    fourPlayersBtn.id = 'fourPlayersBtn';
    fourPlayersBtn.textContent = '4 Players';
    
    let heightPlayersBtn = document.createElement('button');
    heightPlayersBtn.type = 'button';
    heightPlayersBtn.className = 'btn btn-outline-info mx-1';
    heightPlayersBtn.id = 'heightPlayersBtn';
    heightPlayersBtn.textContent = '8 Players';

    let sixteenPlayersBtn = document.createElement('button');
    sixteenPlayersBtn.type = 'button';
    sixteenPlayersBtn.className = 'btn btn-outline-info mx-1';
    sixteenPlayersBtn.id = 'sixteenPlayersBtn';
    sixteenPlayersBtn.textContent = '16 Players';
    
    // Ajout des boutons à l'élément div des boutons
    div.appendChild(fourPlayersBtn);
    div.appendChild(heightPlayersBtn);
    div.appendChild(sixteenPlayersBtn);

    // Récupération de la section par son ID
    let mySection = document.getElementById('containerGameMenu');

    // Ajout de l'élément div principal à la section spécifiée
    mySection.appendChild(div);
    // init_Tournament_buttons();
    init_Tournament_mode_buttons();
}

function init_Tournament_mode_buttons() {

    const fourPlayersBtn = document.getElementById('fourPlayersBtn');
    const heightPlayersBtn = document.getElementById('heightPlayersBtn');
    const sixteenPlayersBtn = document.getElementById('sixteenPlayersBtn');

    fourPlayersBtn.addEventListener('click', function() {

        fourPlayersBtn.classList.add('disabled');
        fourPlayersBtn.classList.remove('btn-outline-info');
        fourPlayersBtn.classList.add('btn-info');
        heightPlayersBtn.classList.add('disabled');
        sixteenPlayersBtn.classList.add('disabled');

        tournamentSize = 4;
        
        create_Tournament_inputs();
    });

    heightPlayersBtn.addEventListener('click', function() {

        fourPlayersBtn.classList.add('disabled');
        heightPlayersBtn.classList.add('disabled');
        heightPlayersBtn.classList.remove('btn-outline-info');
        heightPlayersBtn.classList.add('btn-info');
        sixteenPlayersBtn.classList.add('disabled');

        tournamentSize = 8;
        
        create_Tournament_inputs();
    });

    sixteenPlayersBtn.addEventListener('click', function() {

        fourPlayersBtn.classList.add('disabled');
        heightPlayersBtn.classList.add('disabled');
        sixteenPlayersBtn.classList.add('disabled');
        sixteenPlayersBtn.classList.remove('btn-outline-info');
        sixteenPlayersBtn.classList.add('btn-info');

        tournamentSize = 16;
        
        create_Tournament_inputs();
    });
}

function create_Tournament_inputs() {

    const div = document.createElement('div');
    div.id = 'inputDiv';
    const hr = document.createElement('hr');
    hr.classList = 'text-info my-4';
    div.appendChild(hr);

    let playerNb = 0;
    for (let i = 0; i < (tournamentSize / 2); i++) {
        const inputDiv = document.createElement('div');
        inputDiv.classList = 'col d-flex justify-content-center m-2';
        for (let j = 0; j < 2; j++) {

            playerNb++;
            const input = document.createElement('input');
            input.classList = 'form-control border-info m-1';
            input.type = 'text';
            input.name = 'playerName' + playerNb;
            input.id = 'playerName' + playerNb;
            input.placeholder = 'Player ' + playerNb;
            inputDiv.appendChild(input);
        }
        div.appendChild(inputDiv);
    }
    // Creation du bouton
    const divBtn = document.createElement('div');
    divBtn.className = 'col d-flex justify-content-center mt-2';
    divBtn.id = 'divBtn';
    let playBtn = document.createElement('button');
    playBtn.type = 'button';
    playBtn.className = 'btn btn-outline-success w-25 mb-3 mt-3 p-2';
    playBtn.id = 'playBtn';
    playBtn.textContent = 'Play';

    divBtn.appendChild(playBtn);
    div.appendChild(divBtn);
    const targetContainer = document.getElementById('containerGameMenu');
    targetContainer.appendChild(div);

    initPlayBtn();

}