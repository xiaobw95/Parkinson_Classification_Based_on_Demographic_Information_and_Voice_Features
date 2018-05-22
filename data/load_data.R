filenames <- list.files("parkinsonArff", pattern="*.arff", full.names=TRUE)
for (i in 1:length(filenames)){
  temp<-read.arff(filenames[i])
  voi<-rbind(voi,temp)
}

for (k in 1:length(healthId)){
  if (as.character(voice[1,]$healthCode)==as.character(healthId[k])){
    extend=data_parkinson[k,]
    break
  }
}
i=2; j=2
while (i<=length(filenames)&j<=nrow(voice)) {
  if (grepl(as.character(voice[j,]$audio_audio.m4a),as.character(filenames[i]))){
    for (k in 1:length(healthId)){
      if (as.character(voice[j,]$healthCode)==as.character(healthId[k])){
        extend=rbind(extend,data_parkinson[k,])
        break
      }
    }
    i=i+1  
  }
  j=j+1
}

FN<-function(x) substring(x,26,32)
fn<-lapply(filenames,FN)
fn<-unlist(fn)
fn<-as.integer(fn)

label<-c()
for (i in 1:nrow(extend)){
  label<-c(label,ifelse(parkinson[which(parkinson$X==extend[i,]$X),]$diag=='FALSE',0,1))
}
