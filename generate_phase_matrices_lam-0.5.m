global N omega a

N=100;
tspan=0:0.01:400;
phases=[];

% keeping lambda=0.5 from r vs lam plot
lamda=0.5;

% select which to find phase matrix for: all erdos-reyni("er") graphs or all scale free("sf") graphs
graph_type= "er";

omega=generate_random(0.5,N);

labels=[];
for i=1:250
    y0=(generate_random(pi,N))';
    if graph_type== "er"
    a = readmatrix(sprintf('ER+SF_New/er%i.txt', i)); 
    else
    a = readmatrix(sprintf('ER+SF_New/sf%i.txt', i));
    end   
    [t,y]=ode45(@(t,y)odefm(t,y,lamda),tspan,y0);
    pp=[];
    y=wrapToPi(y);
    pp=[pp,y(40000,:)];
    phases=[phases;pp];    
end

if graph_type== "er"
writematrix(phases,'erphases.txt')
else
writematrix(phases,'sfphases.txt')
end

function rr=generate_random(range,no_points)
rr=range*rand(no_points,1);
for i=1:no_points
   if(rand(1,1)<0.5)
   rr(i)=-rr(i);
   end
end
end

function theta_dot = odefm(~,theta,lamda)
     global omega a
     theta_dot = omega + lamda*sum(a.*sin(theta-theta'))';
end

function r=order_par(x)
global N
r1=abs((sum(exp(1i*x),2))/N);
R=mean(r1);
r=R;
end
