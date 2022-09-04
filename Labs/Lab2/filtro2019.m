function imagemfiltrada=filtro2019()
% a funcao 'filtro2019' pede ao user para escolher uma imagem para filtrar e 
% o tipo de filtro que quer aplicar ? imagem.
% Usa a fun??o built-in 'fspecial' para criar o filtro.
% Podem-se experimentar v?rios tipos de filtros (j? implementados no Matlab):
% 'motion' para dar efeito de movimento a imagem
% 'average' e/ou 'gaussian' para fazer uma filtragem passa-baixo
% 'prewitt', 'sobel' ou 'unsharp" para realcar contornos
% A dimensao do filtro por omissao ? de 3x3. Use valores de 3 a 10.
% Apresenta e devolve a imagem filtrada. 

close all;

disp('Seleccione uma imagem');
[filename, pathname] = uigetfile('*.*', 'abra imagem');
   
fullname=fullfile(pathname,filename);

I=imread(fullname);
%figure(1); imshow(I); title('imagem original');

disp(' Tipo de filtro? (average, gaussian, motion, sobel, prewitt, ...)');
tipo_filtro=input(' filtro?')
disp(' Dimensao n do filtro? (nxn de 3x3 at? 20x20)');
dim=input(' dim?')


switch tipo_filtro
    case {'prewitt','sobel'}
        filtro=fspecial(tipo_filtro);
        IfiltradaHorizontal=imfilter(I,filtro,'replicate');
        IfiltradaVertical=imfilter(I,filtro','replicate');
        Ifiltrada=IfiltradaHorizontal+IfiltradaVertical;
        figure(2)
        subplot(1,2,1), imshow(IfiltradaHorizontal); title('imagem filtrada prewitt horizontal');
        subplot(1,2,2), imshow(IfiltradaVertical); title('imagem filtrada prewitt vertical');
     otherwise
        filtro=fspecial(tipo_filtro,dim);
        Ifiltrada=imfilter(I,filtro,'replicate');
        %figure(2); imshow(Ifiltrada); title('imagem filtrada');
        imagemfiltrada=Ifiltrada;
end

figure(3)
subplot(1,2,1), imshow(I); title('imagem original');
subplot(1,2,2), imshow(Ifiltrada); title('imagem filtrada');
