import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from '../components/home/home.component';
import {PageNotFoundComponent} from '../components/page-not-found/page-not-found.component';
import {PathResolveService} from '../services/path-resolve/path-resolve.service';
import {paths} from '../configuration/app-paths';
import {AboutComponent} from '../components/about/about.component';
import {ContactComponent} from '../components/contact/contact.component';
import {SimulationComponent} from '../components/simulation/simulation.component';
import {
  SimulationListViewComponent
} from '../components/simulation/simulation-list-view/simulation-list-view.component';
import {SimulationCreateViewComponent} from '../components/simulation/simulation-create-view/simulation-create-view.component';


const routes: Routes = [
  {
    path: '',
    redirectTo: paths.home,
    pathMatch: 'full'
  },
  {
    path: paths.home,
    component: HomeComponent,
  },
    {
    path: paths.simulations,
    component: SimulationComponent,
    children: [
      {
        path: '',
        component: SimulationListViewComponent
      },
      {
        path: paths.create,
        component: SimulationCreateViewComponent
      },
    ]
  },
  {
    path: paths.about,
    component: AboutComponent,
  },
  {
    path: paths.contact,
    component: ContactComponent,
  },
  {
    path: '**',
    resolve: {
      path: PathResolveService
    },
    component: PageNotFoundComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
