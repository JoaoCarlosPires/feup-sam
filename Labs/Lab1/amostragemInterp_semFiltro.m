% Esta fun??o faz a sub-amostragem de um ficheiro de audio n?o comprimido
%por um factor k e a sua interpola??o pelo mesmo factor para repor o
%n?mero de amostras. A interpola??o ? feita pela repeti??o de cada amostra k vezes.
% N?o utiliza pr?-filtragem.
% Baseado em down4up4_nofilt de Yao Wang, Polytechnic University, 1/11/2004

function[]=amostragemIntero_semFiltro(ficheiroOriginal,ficheiroInterpolado,k)

fprintf('\n Importar o som original\n');
[y,fs]=audioread(ficheiroOriginal);

%verificar numero de canais (estereo ou mono). Se estereo, usar apenas um
%canal (adicionado em Fev 2022)
info=audioinfo(ficheiroOriginal);
if info.NumChannels>1
    y=y(:,1);
end

% tornar a sequencia multipla de k
orig_length=length(y); N=floor(orig_length/k)*k; y = y(1:N);

% tocar a musica original e mostrar a sua forma de onda
sound(y,fs); %plays the sound
figure(1);
subplot(1,2,1), bar(y(2000:2060),0.02), title('forma de onda original'); % shows values of the 
% samples of the signal, between instant 0.0417s and 0.0429s
% note that the sample values may have negative values. A reasonable representation to choose is to
% consider the ambient pressure zero, with higher and lower pressures being positive and negative.
% Another reasonable representation is to take ambient pressure as half-scale, with lower pressures 
% below and higher pressures above half. Remember that Sound is fundamentally a pressure wave,
% made up of "peaks" which are regions of pressure higher than the ambient pressure and "troughs" 
% which are regions of pressure lower than the ambient pressure. Whether a signed or unsigned 
% representation is used is only a matter of history and convention. 16-bit audio is usually 
% represented as signed but 8-bit audio is usually not.

axis tight; % sets the axis limits to the range of the data.

% constroi e mostra o espectro do sinal de som usando freqz
npfft=4096; %nº de pontos para o espectro
T=1/fs;
t=[0:T:0.04-T]; % 40 milissegundos de sinal correspondentes a 1920 amostras
[H, W] = freqz(y, 1.0, npfft, fs); 
subplot(1,2,2), plot(W, abs(H));
xlabel('Frequencia (Hz)');
ylabel('Magnitude');
title('Espectro do sinal de entrada');

fprintf('\n Carregue numa tecla para continuar\n');
pause

% sub-amostragem sem filtro: reter uma em cada k amostras
fprintf('\n O som sub-amostrado\n');
x=y(1:k:N);
%reproduzir e mostrar o som sub-amostrado
sound(x,fs/k);
figure(2);
subplot(1,2,1),bar(x(2000/k:2060/k),0.02);
axis tight;
title('forma de onda sub-amostrada');
%mostrar o espectro
npfft=2048;
T=1/fs;
t=[0:T:0.04-T]; % 40 milissegundos de sinal
[H, W] = freqz(x, 1.0, npfft, fs); 
subplot(1,2,2), plot(W, abs(H));
xlabel('Frequ?ncia (Hz)');
ylabel('Magnitude');
title('Espectro do sinal sub-amostrado');

fprintf('\n Carregue numa tecla para continuar\n');
pause

%interpolacao para repor numero de amostras (repete k vezes cada amostra)
fprintf('\n O som interpolado\n');
z=zeros(N,1);
%copia cada amostra de x para z k vezes cada
for(i=0:1:k-1)
    z(1+i:k:N)=x;
end

%toca e mostra o som interpolado
sound(z,fs);
figure(3);
subplot(1,2,1),bar(z(2000/k:2060/k),0.02);
axis tight;
title('forma de onda interpolada');
%mostrar o espectro
npfft=2048;
T=1/fs;
t=[0:T:0.04-T]; % 40 milissegundos de sinal
[H, W] = freqz(z, 1.0, npfft, fs); 
subplot(1,2,2), plot(W, abs(H));
xlabel('Frequ?ncia (Hz)');
ylabel('Magnitude');
title('Espectro do sinal interpoladoo');

fprintf('\n Carregue numa tecla para continuar\n');
pause

%guarda sinal interpolado
audiowrite(ficheiroInterpolado,z,fs);

% Calcular o erro quadratico medio MSE e PSNR (Peak Signal to Noise Ratio)
% usa apenas as N amostras do sinal original, N multiplo de k
crop=y(1:1:N);
D=crop-z;
MSE=mean(D.^2);
MSE2 = sum(sum((crop - z).^2))/N;
MAXy=max(y);
PSNR = 10*log10((double(MAXy^2))/MSE2);
fprintf('\nErro entre o sinal original e o interpolado = %g\n\n',MSE);
fprintf('\nPSNR do sinal interpolado = %g\n\n',PSNR);

