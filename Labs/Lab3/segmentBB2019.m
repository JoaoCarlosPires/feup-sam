function segmentBB2019Blueness (outputImage)
% this function receives the name of a file to store the fused image. 
% It starts by segmenting a selected input image based on color,
% and it represents the segmented image as a BW image (foreground in white).
% It then colors the foreground image (the objects)and presents it.
% It finalises by asking the user to select a second image representing the
% new background and fuses the colored foreground with this second image. 
% It stores the fused image in the file passed as an argument.

close all;
disp('Seleccione uma imagem');
[filename, pathname] = uigetfile('*.*', 'abra imagem');
fullname=fullfile(pathname,filename);
image=imread(fullname);

% get image dimensions: an RGB image has three planes
[height, width, planes] = size(image); 

if(planes==3)
    r = image(:, :, 1);         % red channel
    g = image(:, :, 2);         % green channel
    b = image(:, :, 3);          % blue channel


figure(1), imshow([r g b]), title('RGB components');

figure(2),imhist(uint8(b)), title('Blue channel histogram');;
threshold=input('Which threshold?'); % ask the user for a threshold

% BW segmentation: a new matrix with dimensions "height" and "width"
% will have white pixels in the locations corresponding to 
% the B matrix with low values (which will be the foreground)

BWforeground=zeros(height, width);
for i=1:height
    for j=1:width
        if(b(i,j)<threshold) BWforeground(i,j)=255;
        end
    end
end
figure(3), imshow(BWforeground),title('B&W segmented image');

% obtain the full color representation of the foreground objects
foregroundR=zeros(height, width);
foregroundG=zeros(height, width);
foregroundB=zeros(height, width);
for i=1:height
    for j=1:width
        if(BWforeground(i,j)==255)
            foregroundR(i,j)=r(i,j);
            foregroundG(i,j)=g(i,j);
            foregroundB(i,j)=b(i,j);
        end
    end
end
foregroundRGB=cat(3,uint8(foregroundR),uint8(foregroundG),uint8(foregroundB));
figure(4), imshow(foregroundRGB),title('coloured foreground');

%%%%%%%%%%%%%
% alternative using the blueness factor
%%%%%%%%%%%%%
blueness = double(b) - max(double(r), double(g));
% visualize the blueness image
figure(5), imshow(uint8(blueness)), title('blueness channel'); 
%decide the threshold
figure(6),imhist(uint8(blueness)), title('blueness channel histogram');
threshold=input('Which threshold?'); % ask the user for a threshold

BWforegroundBlueness=ones(height,width);

BWforegroundBlueness=blueness<threshold;

figure(7), imshow(BWforegroundBlueness), title('B&W segmented image using blueness');

% obtain the full color representation of the foreground objects
foregroundR=zeros(height, width);
foregroundG=zeros(height, width);
foregroundB=zeros(height, width);

for i=1:height
    for j=1:width
        if(blueness(i,j)<threshold)
            foregroundR(i,j)=r(i,j);
            foregroundG(i,j)=g(i,j);
            foregroundB(i,j)=b(i,j);
        end
    end
end
foregroundRGB=cat(3,uint8(foregroundR),uint8(foregroundG),uint8(foregroundB));
figure(8), imshow(foregroundRGB),title('coloured foreground using blueness');

%%%%%%%%%%%%%%
% creating a new image by superimposing the segmentated objects
%%%%%%%%%%%%%%

%close all;
%disp('Seleccione uma imagem com novo background');
%[filename2, pathname2] = uigetfile('*.*', 'abra imagem');
%fullname2=fullfile(pathname2,filename2);
%image2=imread(fullname2);
%outputImage=imfuse(image2,foregroundRGB);
%figure(7), imshow(uint8(outputImage)),title('fused image');
end

