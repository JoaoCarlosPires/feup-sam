function plotImageSpectrum(img)
%note: the psd can only be calculated seperately for each color channel of
%an RGB image or for the brightness channel. This measn that the input 
%parameter img must be a
%single 2D matrix
psd = 10*log10(abs(fftshift(fft2(img))).^2 );
figure();
mesh(psd);