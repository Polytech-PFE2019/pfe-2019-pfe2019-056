import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AboutComponent } from './about/about.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {ServiceApi} from '../service/service.api';
import {HttpClientModule} from '@angular/common/http';
import {RouterModule, Routes} from '@angular/router';
import { ReponseComponent } from './reponse/reponse.component';
import { FormulaireComponent } from './formulaire/formulaire.component';
import { InstanceComponent } from './instance/instance.component';


const appRoutes:Routes=[

  {path:'about',component:AboutComponent},
  {path:'reponse',component:ReponseComponent},
  {path:'form',component:FormulaireComponent},
  {path:'instance',component:InstanceComponent},


  {
    path: '', redirectTo:'/about',
    pathMatch: 'full'
  }

]


@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    ReponseComponent,
    FormulaireComponent,
    InstanceComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [ServiceApi],
  bootstrap: [AppComponent]
})
export class AppModule { }
