from musicapp import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import null, desc
from sqlalchemy import exc, or_
from flask import Flask,render_template,url_for,request,redirect,flash,abort, jsonify
from musicapp.models import*
import json
from datetime import datetime
now = datetime.now()



import re

date = datetime.now()

@app.route('/')
def rootType():  
    return json.dumps({'error':True,'issue':'Path not match, Root are Song, Podcast, Audiobook'}), 500, {'ContentType':'application/json'}


@app.route('/<string:audioFileType>')# get all row
def dashboard(audioFileType):

    if audioFileType=='Song':
        song_query=Music_table.query.all()
        all_song=[]
        for sng in song_query:
            all_song.append({'song_id': sng.song_id,'song_name': sng.song_name,'duration': sng.duration,'created_date': sng.created_date})
        return jsonify(all_song)

    if audioFileType=='Podcast':
        pod_query=Podcast.query.all()
        all_pod=[]
        for pod in pod_query:
            all_pod.append({'pod_id':pod.pod_id,'pod_name':pod.pod_name,'duration':pod.duration,'upload_time':pod.upload_time,'host':pod.host,'participant':pod.participant})
        return jsonify(all_pod)
          
    if audioFileType=='Audiobook':
        audio_query=Audio.query.all()
        all_audio=[]
        for audio in audio_query:
            all_audio.append({'audio_id':audio.audio_id,'audio_title':audio.audio_title,'narrator':audio.narrator,'duration':audio.duration,'upload_time':audio.upload_time})
        return jsonify(all_audio)


@app.route('/<string:audioFileType>/<int:ids>')# get single row
def single_row(audioFileType,ids):
    if audioFileType=='Song':
        song_query=Music_table.query.filter_by(song_id=ids).first()
        if song_query=='':
            return json.dumps({'error':True,'issue':'Song id not match .Please check and try again'}), 500, {'ContentType':'application/json'}
        all_song=[]
        all_song.append({'song_id': song_query.song_id,'song_name': song_query.song_name,'duration': song_query.duration,'created_date': song_query.created_date})
        return jsonify(all_song)

    if audioFileType=='Podcast':
        pod_query=Podcast.query.filter_by(pod_id=ids).first()
        if pod_query=='':
            return json.dumps({'error':True,'issue':'Pod id not match .Please check and try again'}), 500, {'ContentType':'application/json'}
        all_pod=[]
        all_pod.append({'pod_id':pod_query.pod_id,'pod_name':pod_query.pod_name,'duration':pod_query.duration,'upload_time':pod_query.upload_time,'host':pod_query.host,'participant':pod_query.participant})
        return jsonify(all_pod)
          
    if audioFileType=='Audiobook':
        audio_query=Audio.query.filter_by(audio_id=ids).first()
        if audio_query=='':
            return json.dumps({'error':True,'issue':'Audio id not match . Please check and try again'}), 500, {'ContentType':'application/json'}
        all_audio=[]
        all_audio.append({'audio_id':audio_query.audio_id,'audio_title':audio_query.audio_title,'narrator':audio_query.narrator,'duration':audio_query.duration,'upload_time':audio_query.upload_time})
        return jsonify(all_audio)             
    



@app.route('/<string:audioFileType>',methods=['POST']) #insert row
def music_inst(audioFileType):
    request_data = request.get_json()

    if audioFileType=='Song':
         
        song_id=request_data["song_id"]
        if song_id=='':
            return json.dumps({'error':True,'issue':'Song id should not be empty'}), 500, {'ContentType':'application/json'}    
               
        song_name=request_data["song_name"]
        if song_name=='':
            return json.dumps({'error':True,'issue':'Song name should not be empty'}), 500, {'ContentType':'application/json'}
        elif len(str(song_name)) > 100:
            return json.dumps({'error':True,'issue':'Song name should not be greater than 100 character'}), 500, {'ContentType':'application/json'}

        duration=request_data["duration"]
        if duration=='':
            return json.dumps({'error':True,'issue':'Duration should not be empty'}), 500, {'ContentType':'application/json'}
        elif duration<=0:   
            return json.dumps({'error':True,'issue':'Duration should not be null or negative'}), 500, {'ContentType':'application/json'}

        dte=now.strftime("%d/%m/%Y %H:%M:%S")
        
        if dte=='':
            return json.dumps({'error':True,'issue':'Date should not be empty'}), 500, {'ContentType':'application/json'}
        
        try:
            music_insert=Music_table(song_id=song_id,song_name=song_name,duration=duration,created_date=dte)
            db.session.add(music_insert)
            db.session.commit()
            if music_insert:
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        except Exception as e:
             return json.dumps({'success':False,'message':str(e)}), 500, {'ContentType':'application/json'} 

        
      


    
    if audioFileType=='Podcast':
        pod_id=request_data["pod_id"]
        if pod_id=='':
            return json.dumps({'error':True,'issue':'Pod id should not be empty'}), 500, {'ContentType':'application/json'} 
              
        pod_name=request_data["pod_name"]

        song_name=request_data["song_name"]
        if pod_name=='':
            return json.dumps({'error':True,'issue':'Pod name should not be empty'}), 500, {'ContentType':'application/json'}
        elif len(str(pod_name)) > 100:
            return json.dumps({'error':True,'issue':'Pod name should not be greater than 100 character'}), 500, {'ContentType':'application/json'}

        

        duration=request_data["duration"]
        if duration=='':
            return json.dumps({'error':True,'issue':'Duration should not be empty'}), 500, {'ContentType':'application/json'}
        elif duration<=0:   
            return json.dumps({'error':True,'issue':'Duration should not be null or negative'}), 500, {'ContentType':'application/json'}

        dte=now.strftime("%d/%m/%Y %H:%M:%S")
        if dte=='':
            return json.dumps({'error':True,'issue':'Date should not be empty'}), 500, {'ContentType':'application/json'}

        host=request_data["host"]
        if host=='':
            return json.dumps({'error':True,'issue':'host should not be empty'}), 500, {'ContentType':'application/json'}

        Participant=request_data["participant"]
   
        if Participant=='':
            return json.dumps({'error':True,'issue':'host should not be empty'}), 500, {'ContentType':'application/json'}

        try:
            pod_insert=Podcast(pod_id=pod_id,pod_name=pod_name,duration=duration,upload_time=dte,host=host,participant=Participant)
            db.session.add(pod_insert)
            db.session.commit()
            if pod_insert:
              
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        except Exception as e:
             return json.dumps({'success':False,'message':str(e)}), 500, {'ContentType':'application/json'}



    if audioFileType=='Audiobook':

        audio_id=request_data["audio_id"]
        if audio_id=='':
            return json.dumps({'error':True,'issue':'Pod id should not be empty'}), 500, {'ContentType':'application/json'} 
              
        audio_title=request_data["audio_title"]
        if audio_title=='':
            return json.dumps({'error':True,'issue':'pod name should not be empty'}), 500, {'ContentType':'application/json'}
        elif len(str(pod_name)) > 100:
            return json.dumps({'error':True,'issue':'Pod name should not be greater than 100 character'}), 500, {'ContentType':'application/json'}
        
        narrator=request_data["narrator"]
    
        duration=request_data["duration"]
        if duration=='':
            return json.dumps({'error':True,'issue':'Duration should not be empty'}), 500, {'ContentType':'application/json'}
        elif duration<=0:   
            return json.dumps({'error':True,'issue':'Duration should not be null or negative'}), 500, {'ContentType':'application/json'}

        dte=now.strftime("%d/%m/%Y %H:%M:%S")
        if dte=='':
            return json.dumps({'error':True,'issue':'Date should not be empty'}), 500, {'ContentType':'application/json'}

        try:
            audio_insert=Audio(audio_id=audio_id,audio_title=audio_title,narrator=narrator,duration=duration,upload_time=dte)
            db.session.add(audio_insert)
            db.session.commit()
            if audio_insert:  
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
            
        except Exception as e:
             return json.dumps({'success':False,'message':str(e)}), 500, {'ContentType':'application/json'}





@app.route('/<string:audioFileType>/<int:ids>',methods=['PUT']) #update row
def music_updte(audioFileType,ids):
    request_data = request.get_json()

    if audioFileType=='Song':

        song_id=request_data["song_id"]
    
        if song_id=='':
            return json.dumps({'error':True,'issue':'Song id should not be empty'}), 500, {'ContentType':'application/json'}       
        song_name=request_data["song_name"]
        if song_name=='':
            return json.dumps({'error':True,'issue':'Song name should not be empty'}), 500, {'ContentType':'application/json'}
        elif len(str(song_name)) > 100:
            return json.dumps({'error':True,'issue':'Song name should not be greater than 100 character'}), 500, {'ContentType':'application/json'}

        duration=request_data["duration"]
        if duration=='':
            return json.dumps({'error':True,'issue':'Duration should not be empty'}), 500, {'ContentType':'application/json'}
        elif duration<=0:   
            return json.dumps({'error':True,'issue':'Duration should not be null or negative'}), 500, {'ContentType':'application/json'}

        dte=now.strftime("%d/%m/%Y %H:%M:%S")
        
        if dte=='':
            return json.dumps({'error':True,'issue':'Date should not be empty'}), 500, {'ContentType':'application/json'}
        try:
            music_update=Music_table.query.filter_by(song_id=ids).update(dict(song_id=song_id,song_name=song_name,duration=duration,created_date=dte))
            db.session.commit()
        
            if music_update:
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        except Exception as e:
             return json.dumps({'success':False,'message':str(e)}), 500, {'ContentType':'application/json'}


    
    if audioFileType=='Podcast':
        pod_id=request_data["pod_id"]
        if pod_id=='':
            return json.dumps({'error':True,'issue':'Pod id should not be empty'}), 500, {'ContentType':'application/json'} 
              
        pod_name=request_data["pod_name"]

        if pod_name=='':
            return json.dumps({'error':True,'issue':'pod name should not be empty'}), 500, {'ContentType':'application/json'}

        duration=request_data["duration"]
        if duration=='':
            return json.dumps({'error':True,'issue':'Duration should not be empty'}), 500, {'ContentType':'application/json'}
        elif duration<=0:   
            return json.dumps({'error':True,'issue':'Duration should not be null or negative'}), 500, {'ContentType':'application/json'}

        dte=now.strftime("%d/%m/%Y %H:%M:%S")
        if dte=='':
            return json.dumps({'error':True,'issue':'Date should not be empty'}), 500, {'ContentType':'application/json'}

        host=request_data["host"]
        if host=='':
            return json.dumps({'error':True,'issue':'host should not be empty'}), 500, {'ContentType':'application/json'}

        Participant=request_data["participant"]
   
        if Participant=='':
            return json.dumps({'error':True,'issue':'host should not be empty'}), 500, {'ContentType':'application/json'}

        try:
            pod_update=Podcast.query.filter_by(pod_id=ids).update(dict(pod_id=pod_id,pod_name=pod_name,duration=duration,upload_time=dte,host=host,participant=Participant))
            db.session.commit()
       
            if pod_update:
              
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        except Exception as e:
             return json.dumps({'success':False,'message':str(e)}), 500, {'ContentType':'application/json'}
        

    if audioFileType=='Audiobook':

        audio_id=request_data["audio_id"]
        if audio_id=='':
            return json.dumps({'error':True,'issue':'Pod id should not be empty'}), 500, {'ContentType':'application/json'} 
              
        audio_title=request_data["audio_title"]
        if audio_title=='':
            return json.dumps({'error':True,'issue':'pod name should not be empty'}), 500, {'ContentType':'application/json'}
        elif len(str(pod_name)) > 100:
            return json.dumps({'error':True,'issue':'Pod name should not be greater than 100 character'}), 500, {'ContentType':'application/json'}

        
        narrator=request_data["narrator"]
    
        duration=request_data["duration"]
        if duration=='':
            return json.dumps({'error':True,'issue':'Duration should not be empty'}), 500, {'ContentType':'application/json'}
        elif duration<=0:   
            return json.dumps({'error':True,'issue':'Duration should not be null or negative'}), 500, {'ContentType':'application/json'}


        dte=now.strftime("%d/%m/%Y %H:%M:%S")
        if dte=='':
            return json.dumps({'error':True,'issue':'Date should not be empty'}), 500, {'ContentType':'application/json'}
        try:
            audio_update=Audio.query.filter_by(audio_id=ids).update(dict(audio_id=audio_id,audio_title=audio_title,narrator=narrator,duration=duration,upload_time=dte))
            db.session.commit()    
        
            if audio_update:
          
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        except Exception as e:
             return json.dumps({'success':False,'message':str(e)}), 500, {'ContentType':'application/json'}


@app.route('/<string:audioFileType>/<int:ids>',methods=['DELETE']) #delete row
def del_music(audioFileType,ids):
    if audioFileType=='Song':
        del_query=Music_table.query.filter_by(song_id=ids).first()
        db.session.delete(del_query)
        db.session.commit()
        if del_query:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        else:
            return json.dumps({'error':True,'issue':'Data not deleted '}), 500, {'ContentType':'application/json'}

    if audioFileType=='Podcast':
        del_query=Podcast.query.filter_by(pod_id=ids).first()
        db.session.delete(del_query)
        db.session.commit()
        if del_query:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        else:
            return json.dumps({'error':True,'issue':'Data not deleted '}), 500, {'ContentType':'application/json'}

    if audioFileType=='Audiobook':
        del_query=Audio.query.filter_by(audio_id=ids).first()
        db.session.delete(del_query)
        db.session.commit()
        if del_query:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
        else:
            return json.dumps({'error':True,'issue':'Data not deleted '}), 500, {'ContentType':'application/json'}
     
    
