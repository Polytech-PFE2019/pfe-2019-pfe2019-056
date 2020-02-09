import { Component, OnInit } from '@angular/core';
import {ServiceApi} from '../../service/service.api';
import {Router} from '@angular/router';

@Component({
  selector: 'app-reponse',
  templateUrl: './reponse.component.html',
  styleUrls: ['./reponse.component.css']
})
export class ReponseComponent implements OnInit {

  response:any=[];
  reponseConflicts;
  c: any;
  mode=1
  ACM
  constructor(private serviceApi:ServiceApi,private router:Router) {

  }

  ngOnInit() {


    this.serviceApi.responseData
      .subscribe(data=>{
        this.response=data;
        this.getConflicts()
        //console.log(this.response[0][1])
      },error => {
        console.log(error);
      })
  }

  getConflicts () {

    this.serviceApi.getConflicts()
  .subscribe(dataCon=>{
      this.reponseConflicts=dataCon;
      console.log(this.reponseConflicts)
      //console.log(this.response[0][1])
    },error => {
      console.log(error);
    })
  }
  goToPage() {

    this.router.navigate(['about']);
  }

  onSubmit(conflict) {
    console.log(conflict)
    this.serviceApi.getAcm(conflict)
      .subscribe(dataAcm=>{
        this.ACM=dataAcm;
        console.log(this.ACM)
      },error => {
        console.log(error);
      })
    this.mode=2
    //this.ACM="je suis l'ACM qui va régeler le probleme"

  }
}
