import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseurl = "http://akrobat.shubs.de/";
  httpHeaders = new HttpHeaders({'Content-type': 'aplication/json'});
  constructor( private http: HttpClient) { }

 getAllExercises(): Observable<any>{
   return this.http.get(this.baseurl + 'exercises/', {headers: this.httpHeaders});
}
getOneExercise(id): Observable<any>{
   return this.http.get(this.baseurl + 'exercises/' + id + "/", {headers: this.httpHeaders});
}


}
