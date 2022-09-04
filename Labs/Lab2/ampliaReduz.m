function [resultado1,resultado2] = ampliaReduz (N, factor, metodo);

% fun??o para ampliar ou reduzir dimensoes espaciais da imagem "zone-plate"
% Recebe as dimensoes N da imagem de teste a construir, 
% o factor de ampliacao/reducao para aplicar ? imagem de teste criada,
% e ainda um valor numerico para indicar o metodo de interpola??o a usar:
% 1: nearest neighbor; 2) bilinear; 3: bicubic
% Usa a fun??o built-in imresize(I, scale,'method') do Matlab
% Usa a fun??o "imzoneplate(N)"
% Retorna as imagens reduzidas ou ampliadas pelos dois m?todos

%Nota: os titulos das figuras nao estao a aparecer correctamente!!!

Z=imzoneplate(N);
figure, imshow(Z), title('imagem Z de teste original');

% se se tratar de uma redu??o (factor<1) obtem a imagem apenas por
% elimina??o de amostras e depois usa imresize
if factor<1
    factorReducao=1/factor;
    Zreduzida = Z(1:factorReducao:end,1:factorReducao:end);
    figure, imshow(Zreduzida), title('imagem reduzida por eliminacao');
    
% agora obtem nova imagem reduzida usando imresize com o metodo escolhido
    switch metodo
        case 1,
            ZreduzidaMatlab=imresize(Z,factor,'nearest');
        case 2,
            ZreduzidaMatlab=imresize(Z,factor,'bilinear');
        case 3,
            ZreduzidaMatlab=imresize(Z,factor,'bicubic');
    end
    figure, imshow(ZreduzidaMatlab), title('Zreduzida com imresize');
    % retorna as imagens reduzidas com os dois m?todos
    resultado1=Zreduzida;
    resultado2=ZreduzidaMatlab;

else
    % come?a por ampliar apenas por repeticao de pixels criando uma matriz
    % de zeros com as dimensoes desejadas
    Zampliada=zeros(factor*N,factor*N);   
    for(i=1:1:N)
        for(j=1:1:N)
            for(k=(factor*i)-1:1:(factor*i)-1+(factor-1))
                for(l=(factor*j)-1:1:(factor*j)-1+(factor-1))
                    Zampliada(k,l)=Z(i,j);
                end
            end
        end
    end
    figure, imshow(Zampliada), title('Z ampliada por repeticao');
    
    % agora amplia usando imresize com o m?todo escolhido
    switch metodo
        case 1,
            ZampliadaMatlab=imresize(Z,factor,'nearest');
        case 2,
            ZampliadaMatlab=imresize(Z,factor,'bilinear');
        case 3,
            ZampliadaMatlab=imresize(Z,factor,'bicubic');
    end
    figure, imshow(ZampliadaMatlab), title('Z ampliada com imresize');
% retorna as imagens ampliadas com os dois m?todos
resultado1=Zampliada;
resultado2=ZampliadaMatlab;
end

