function Idenoised=filtroMediana();

close all;

disp('Seleccione uma imagem');
[filename, pathname] = uigetfile('*.*', 'abra imagem');
   
fullname=fullfile(pathname,filename);

I=imread(fullname);
figure(1); imshow(I); title('imagem original');

if size(I,3) == 3
    J=rgb2ycbcr(I);
    I=J(:,:,1);
end

promptMessage = sprintf('a imagem tem ruido?');
	button = questdlg(promptMessage, 'a imagem tem ruido?', 'Sim', 'Nao', 'Sim');

if strcmp(button, 'Nao')
     disp('vamos introduzir algum ruido');
     disp('introduza % de ruido (valor decimal inferior a 1):');
     r=input('% ruido? ');
     IR = imnoise(I,'salt & pepper',r);
else
    IR=I;
end

Idenoised=medfilt2(IR);

figure(2), imshow(IR); title('imagem com ruido');
figure(3), imshow(Idenoised); title('imagem sem ruido');